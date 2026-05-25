---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

An etching of some aquatic beast dragging a figure beneath the waves adorns the ivory of a whelming scrimshaw. When you Activate this item, you break it and choose one creature within 30 feet. The target must attempt a DC 30 [[Fortitude]] save; amphibious and aquatic creatures are immune.
- **Critical Success** The creature is unaffected.
- **Success** The target becomes [[Sickened]] 1 and unable to breathe until this sickened condition ends.
- **Failure** As success, but [[Sickened]] 2.
- **Critical Failure** As success, but [[Sickened]] 3.

**Source:** `= this.source` (`= this.source-type`)
