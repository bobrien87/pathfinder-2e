---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Surki|Surki]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your claws are especially hard and can break through earth and predators alike. You gain a claw unarmed attack that deals 1d4 slashing damage. Your claws are in the brawling group and have the agile, finesse, unarmed, and versatile B traits.

- **Evolution** Your wrist nodes project magic into a durable digging wedge. You can spend an Interact action to increase your claw unarmed attack's damage to 1d6; grant it the magical, razing, and versatile force traits; and remove the agile trait. You can spend another action to deactivate the wedge and return your claw to its normal statistics.

- **Evolution** Your ankle nodes can emit grounding claw spikes of magic to hold you in place. If any effect would force you to move 10 feet or more, you can choose to move only half the distance. The extra traction from your claw spikes allows you to Climb with one hand occupied (or with both hands occupied if you have the [[Combat Climber]] feat). You gain the [[Trench Digging]] reaction.

**Source:** `= this.source` (`= this.source-type`)
