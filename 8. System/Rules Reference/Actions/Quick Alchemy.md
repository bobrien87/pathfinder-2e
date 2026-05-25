---
type: action
source-type: "Remaster"
traits: ["[[Alchemist]]", "[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're either holding or wearing an [[Alchemist's Toolkit]]. and you have a free hand.

You can either use up a versatile vial to make another alchemical consumable at a moment's notice or create an especially short-lived versatile vial. Any effect created by an item made with Quick Alchemy that would have a duration longer than 10 minutes lasts for 10 minutes instead.

- **Create Consumable** You expend one of your versatile vials to create a single alchemical consumable item of your level or lower that's in your formula book. You don't have to spend the normal monetary cost in alchemical raw materials or need to attempt a Crafting check. This item has the infused trait, but it remains potent only until the start of your next turn. (As normal, you need only one formula for an item to create any level of that item.)
- **Quick Vial** You create a versatile vial that can be used only as a bomb or for the versatile vial option from your research field (it can't be used to create a consumable, for example). This item has the infused trait, but it remains potent only until the end of your current turn.

**Source:** `= this.source` (`= this.source-type`)
