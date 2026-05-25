---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Consumable]]"]
price: "{'gp': 1}"
usage: "worn-under-armor"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Adventurers have found a number of uses for these animal blood–filled bladders, which were originally used in theatrical productions. Whenever you take slashing or piercing damage with the fake blood pack under your clothes or armor, roll a DC 11 flat check. On a success, the blood pack is punctured. You or an ally can puncture the hidden pack intentionally with an Interact action. When faking an injury, a punctured blood pack grants a +2 item bonus to relevant Deception checks, such as to [[Lie]] about being injured, for 4 hours after the pack has been punctured or until the blood is washed off, whichever comes first. Abilities that trigger when a creature deals bleed damage, that determine if a creature is bleeding, or are otherwise based on bleed damage don't trigger or apply for blood from a fake blood pack, which might mean creatures with such abilities automatically realize the ruse.

**Source:** `= this.source` (`= this.source-type`)
