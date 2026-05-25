---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Divine]]"]
price: "{'gp': 100}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This silver platter and cloche set is intricately carved with scenes of overflowing feast tables. When you speak the command word, a dish is created for your lips and tongue alone. Anyone else who tries to eat the summoned food is compelled to immediately vomit it back up, unchewed and undigested.

**Activate—Savory Feast** 10 minutes (concentrate, exploration, manipulate)

**Frequency** once per week

**Effect** Speaking "savor" as you lift the lid creates a dish you've never tasted before, whether it's the unique delicacy of a far-flung region or the forbidden flesh of a sapient creature. If you spend 10 minutes consuming the entire meal, you regain @Damage[(2d6+8)[healing]] Hit Points and gain a +2 status bonus to saving throws against being sickened for 24 hours, but if you attempt to ingest anything else in that time—including elixirs and potions—you must first succeed at a DC 5 flat check or the action is wasted.

> [!danger] Effect: Platter of Putrid Dreams

**Source:** `= this.source` (`= this.source-type`)
