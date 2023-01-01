# Roadmap For Creating Animations Front-End
For a first prototype, this project will be done in a separated Redux/React/Typescript project. </br>
After the prototypes approval and further understanding of the [The-Via/App](https://github.com/the-via/app) application, it will be integrated into a fork of the original github project.

## Part 1: Rendering A Keyboard To The Screen
From the start we want to use the correct interfaces for the keyboards, and reuse as much of the exiting code as possible. 

The existing [The-Via/App](https://github.com/the-via/app) have already implemented most of the functionality needed for this part. However, currently the displayed keyboard is selected from the connected `HID` device. 

The connected device is saved to the `redux` storage of the application, and the displayed keyboard is constructed from multiple objects that are retrieved from the updated `redux` state. </br>
The way it works is pretty weird, and needs to further researched. At compile time, all the keyboards' data from [The-Via/Keyboards](https://github.com/the-via/keyboards) is saved to the `public/definitions/` folder, and then *somehow* (further research is needed here) `redux` retrieves the connected keyboard `definition` (as it's called there) from its `HID` device ID. This is the part we need to skip and let the user choose whatever keyboard he decides.

If we finish the mentioned above, we can assume that this part is complete and we can continue to the animation.

- [ ] Understand how the keyboards' [definitions](https://github.com/the-via/app/blob/main/src/store/definitionsSlice.ts) are passed to the application.
- [ ] Create a keyboard selection dropdown using via-keyboards repo (this will ensure working with the correct interfaces), selecting one of the definitions created above.
- [ ] Understand how to [`PositionedKeyboard`](https://github.com/the-via/app/blob/main/src/components/positioned-keyboard.tsx) component works and how the data is passed from [`redux`].
- [ ] Render the selected keyboard using a modified version of the `PositionedKeyboard` from the previous step.

## Part 2: Adding Basic Interactive Interface
After rendering the keyboard to the screen, we want to be able to simulate the keyboard's `RGB` lighting. For this step, we can be satisfied by giving a selected key some solid color. The selection can from a mouse click or from the actual keyboard keystroke [TBD].

- [ ] fill a selected key with some solid color
- [ ] React to mouse press on key
- [ ] React to key presses from an actual keyboard

## Part 3: Showing Basic Animation
TBD