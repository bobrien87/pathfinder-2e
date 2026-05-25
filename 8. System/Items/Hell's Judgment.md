---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Fire]]", "[[Magical]]", "[[Reach]]", "[[Trip]]"]
price: "{'gp': 10000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** A character who is a member of the Hellknights has access to this weapon.

These massive *+2 flaming greater striking guisarmes* are bestowed only upon the most loyal and renowned Hellknight paravicars, especially those who have distinguished themselves in the service of the strict laws of the organization.

**Activate—Flames of Phlegethon** `pf2:2` (concentrate, divine, manipulate, unholy)

**Frequency** once per day

**Effect** You strike the ground with your axe, tearing open a one-way rift to the fourth layer of Hell in a @Template[type:line|distance:30] that spews a curtain of hellfire. All creatures in the area take @Damage[6d6[fire],6d6[spirit]|options:area-damage]{6d6 fire damage and 6d6 spirit damage} (DC 37 [[Reflex]] save) before the rift vanishes.

**Source:** `= this.source` (`= this.source-type`)
