---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Tripkee|Tripkee]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your tongue is especially long, and you can launch it with extraordinary range and precision. You can use your tongue to deliver spells with a range of touch and perform extremely simple Interact actions, such as opening some types of unlocked doors. Your tongue can't perform actions that require fingers or significant manual dexterity, including any action that would require a check to accomplish, and you can't use it to hold items.

**Source:** `= this.source` (`= this.source-type`)
