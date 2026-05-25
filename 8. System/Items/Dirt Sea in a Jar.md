---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 880}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small jar of dark sand swirls intensely as you peer into it, evoking the dangerous beauty of the Dirt Sea.

**Activate** `pf2:1` or `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You pour the contents of the jar onto unworked ground. If you activate this item with one action, you pour the sand into one or two @Template[line|distance:5]{5-foot squares} adjacent to you. If you activate this item with two actions, the sand spreads across a @Template[type:cone|distance:15]. The affected space turns into [[Quicksand]]. Creatures already in the area can Step out of the area as a reaction. The quicksand doesn't inflict lasting damage to most surfaces or nearby architecture, though a feature surrounded by the quicksand might sink or settle naturally. This terrain lasts for 1 day or until the effect is Dismissed, causing the sand to reappear in the jar.

**Source:** `= this.source` (`= this.source-type`)
