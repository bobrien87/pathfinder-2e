---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Extradimensional]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (manipulate)

This padlock exists in a dormant state while it's closed and its associated key is in the keyhole. To activate this item, you remove the key, which causes the keyhole to become a portal to an extradimensional space. This space can hold a single object of up to 1 Bulk by pressing it against the keyhole. At any point within the next 24 hours, the key can be used to open the lock with an Interact action, which safely releases the item onto the ground in your space.

If the lock isn't opened within the next 24 hours, the key disintegrates, and from then on, a creature who succeeds at a DC 16 [[Thievery]] check can Pick the Lock open to release the item. On a critical failure, the padlock is destroyed and its contents are lost forever

**Source:** `= this.source` (`= this.source-type`)
