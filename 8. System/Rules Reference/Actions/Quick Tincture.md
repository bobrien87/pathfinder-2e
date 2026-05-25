---
type: action
source-type: "Remaster"
traits: ["[[Investigator]]", "[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Cost** 1 versatile vial

**Requirements** You know the formula for the alchemical item you're creating, you are holding or wearing alchemist's toolkit, and you have a free hand.

You quickly brew up a short-lived tincture. You create a single alchemical elixir or tool of your level or lower without having to spend the normal monetary cost in alchemical reagents or needing to attempt a Crafting check. This item has the infused trait, but it remains potent only until the end of the current turn.

**Source:** `= this.source` (`= this.source-type`)
