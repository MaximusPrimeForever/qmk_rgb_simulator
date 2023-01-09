# General Flow of QMK

The interesting directory is `quantum`.  
Inside, we look at `main.c`:
```c
int main(void) {
    platform_setup();
    protocol_setup();
    keyboard_setup();

    protocol_init();

    /* Main loop */
    while (true) {
        protocol_task(); // <<<

#ifdef QUANTUM_PAINTER_ENABLE
        // Run Quantum Painter animations
        void qp_internal_animation_tick(void);
        qp_internal_animation_tick();
#endif

// ...
```

Notice `protocol_task()`. We take a look at it next:
```c
void protocol_task(void) {
    protocol_pre_task();

    keyboard_task(); // <<<

    protocol_post_task();
}
```
Down the rabbit hole we go, into `keyboard_task()` next - located in `quantum/keyboard.c`:
```c
void keyboard_task(void) {
    const bool matrix_changed = matrix_task();
    if (matrix_changed) {
        last_matrix_activity_trigger();
    }

    quantum_task();

#if defined(SPLIT_WATCHDOG_ENABLE)
    split_watchdog_task();
#endif

#if defined(RGBLIGHT_ENABLE)
    rgblight_task();
#endif

#ifdef LED_MATRIX_ENABLE
    led_matrix_task();
#endif

#ifdef RGB_MATRIX_ENABLE
    rgb_matrix_task(); // <<<
#endif

// ...
```
For now we focus on RGB matrices, so ignore `led_matrix_task()`.  
Looking at `rgb_matrix_task` located in `quantum/rgb_matrix/rgb_matrix.c`:
```c
void rgb_matrix_task(void) {
    rgb_task_timers();

    // Ideally we would also stop sending zeros to the LED driver PWM buffers
    // while suspended and just do a software shutdown. This is a cheap hack for now.
    bool suspend_backlight = suspend_state ||
#if RGB_MATRIX_TIMEOUT > 0
                             (rgb_anykey_timer > (uint32_t)RGB_MATRIX_TIMEOUT) ||
#endif // RGB_MATRIX_TIMEOUT > 0
                             false;

    uint8_t effect = suspend_backlight || !rgb_matrix_config.enable ? 0 : rgb_matrix_config.mode;

    switch (rgb_task_state) {
        case STARTING:
            rgb_task_start();
            break;
        case RENDERING:
            rgb_task_render(effect); // <<<
            if (effect) {
                rgb_matrix_indicators();
                rgb_matrix_indicators_advanced(&rgb_effect_params);
            }
            break;
        case FLUSHING:
            rgb_task_flush(effect);
            break;
        case SYNCING:
            rgb_task_sync();
            break;
    }
}
```
`effect` is a `uint8_t` and its value should indicate the effect QMK should render onto the keyboard.   
We look at `rgb_task_render()` located in the same file: 
```c
static void rgb_task_render(uint8_t effect) {
    bool rendering         = false;
    rgb_effect_params.init = (effect != rgb_last_effect) || (rgb_matrix_config.enable != rgb_last_enable);
    if (rgb_effect_params.flags != rgb_matrix_config.flags) {
        rgb_effect_params.flags = rgb_matrix_config.flags;
        rgb_matrix_set_color_all(0, 0, 0);
    }

    // each effect can opt to do calculations
    // and/or request PWM buffer updates.
    switch (effect) {
        case RGB_MATRIX_NONE:
            rendering = rgb_matrix_none(&rgb_effect_params);
            break;

// ---------------------------------------------
// -----Begin rgb effect switch case macros-----
#define RGB_MATRIX_EFFECT(name, ...)          \
    case RGB_MATRIX_##name:                   \
        rendering = name(&rgb_effect_params); \
        break;
#include "rgb_matrix_effects.inc"
#undef RGB_MATRIX_EFFECT

#if defined(RGB_MATRIX_CUSTOM_KB) || defined(RGB_MATRIX_CUSTOM_USER)
#    define RGB_MATRIX_EFFECT(name, ...)          \
        case RGB_MATRIX_CUSTOM_##name:            \
            rendering = name(&rgb_effect_params); \
            break;
#    ifdef RGB_MATRIX_CUSTOM_KB
#        include "rgb_matrix_kb.inc"
#    endif
#    ifdef RGB_MATRIX_CUSTOM_USER
#        include "rgb_matrix_user.inc"
#    endif
#    undef RGB_MATRIX_EFFECT
#endif
            // -----End rgb effect switch case macros-------
            // ---------------------------------------------

        // Factory default magic value
        case UINT8_MAX: {
            rgb_matrix_test();
            rgb_task_state = FLUSHING;
        }
            return;
    }

    rgb_effect_params.iter++;

    // next task
    if (!rendering) {
        rgb_task_state = FLUSHING;
        if (!rgb_effect_params.init && effect == RGB_MATRIX_NONE) {
            // We only need to flush once if we are RGB_MATRIX_NONE
            rgb_task_state = SYNCING;
        }
    }
}
```

The interesting part is the voodoo switch case in the middle of the function.  
The switch case is constructed by using the `#include` mechanism to directly copy code into the function (this explains why RGB animation code is in `.h` files.).  
