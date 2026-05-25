---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Awakened Animal|Awakened Animal]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You are an aquatic animal who is most comfortable in the water. You may spend much of your time in the water like an alligator, seal, whale, or dolphin, or you may require the water to breathe like a fish or some crustaceans.

You have one animal attack of your choice (typically claw, jaws, or tail; see the sidebar). Choose if you are aquatic or water-dwelling.

- **Aquatic:** You gain the aquatic trait and you have a swim Speed of 30 feet. The aquatic trait means you breathe water but not air, and your bludgeoning and slashing unarmed Strikes don't take the usual –2 penalty for being underwater.

- **Water-dwelling:** You can hold your breath underwater for 10 minutes before needing air. You have a swim Speed of 20 feet, and if you can move on land, you have base Speed of 20 feet.

**Source:** `= this.source` (`= this.source-type`)
