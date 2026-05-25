---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 2750}"
usage: "worngarment"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This exquisite scarlet robe embroidered with golden depictions of fiends and their weapons is fashioned after the garb of the cloistered Sisters of the Golden Erinys. The robe's belt is embroidered to look like a snake, complete with metal fangs.

**Activate—Biting Belt** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You remove the robe's belt and snap it at an enemy within your reach. As you do, it briefly animates to bite that foe, dealing 6d8 poison damage with a basic DC 31 [[Fortitude]] save. On a critical failure, the target is also [[Sickened]] 1.

**Source:** `= this.source` (`= this.source-type`)
