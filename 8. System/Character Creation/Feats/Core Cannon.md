---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Arcane]]", "[[Automaton]]", "[[Concentrate]]"]
frequency: "once per day"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Your body transforms into a powerful magical cannon. While immobile as a cannon, you can fire blasts of energy directly from your core, devastating your foes. You become [[Immobilized]] until you use an Interact action to revert back to your standard form. While in your cannon form, the only actions you can use are to Strike with an energy blast unarmed attack or to Interact to revert back to your standard form. You can remain in your cannon form for up to 1 minute or until you take the action to revert back to your standard form, whichever comes first.

Energy blasts are a special ranged unarmed attack. You can only make energy blast Strikes while you're in your cannon form. Your energy blasts deal 3d8 fire damage and 3d6 force damage, which increases to 4d8 fire damage and 3d6 force damage at level 20. You gain the item bonus to attack rolls with your energy blasts from the highest potency rune on any [[Handwraps of Mighty Blows]] you are wearing or any weapon you are wielding, but striking and property runes have no effect on your energy blasts. Energy blasts have a range increment of 120 feet. On a critical hit with an energy blast, the target takes 10 persistent fire damage. Your energy blast doesn't add critical specialization effects. If it matters for an effect dependent on weapon damage dice, an energy blast's number of weapon damage dice is three, or four at level 20.

**Source:** `= this.source` (`= this.source-type`)
