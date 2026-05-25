---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Revenge of the Runelords Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** You designate one of the seven schools of Thassilonian magic—envy, gluttony, greed, lust, pride, sloth, or wrath—and focus your need for revenge against those who serve these ideals. You do not need to be able to see a creature that serves these ideals to make this designation. The designation lasts until your next daily preparations.

You gain a +2 circumstance bonus to Perception checks when you `act seek` a creature that serves these ideals (including an actual runelord, a wizard who follows that school of Thassilonian magic, or any creature you know or suspect serves the interests of that school's particular sin—subject to GM's approval), and a +2 circumstance bonus to Intimidation checks made to `act demoralize` such creatures. Your Strikes also deal 1d4 extra precision to these creatures when they're [[Frightened]].

**Source:** `= this.source` (`= this.source-type`)
