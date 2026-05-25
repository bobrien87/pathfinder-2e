---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 600}"
usage: "affixed-to-unarmored-defense-item"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You would be reduced to 0 Hit Points by damage but not immediately killed

**Requirements** You are unarmored.

This tiny crystal vial of oily liquid is typically attached to a pin or worn on a tether attached to the affixed article of clothing. When you Activate the vial, you avoid being knocked out and remain at 1 Hit Point, your [[Wounded]] condition increases by 1, and the talisman casts [[Drop Dead]] on you. You and any items you're wearing and holding are instantly transported from your current space to a clear space of your choice within 30 feet. You take no damage from the triggering effect. If you are carrying another creature (even one contained inside an extradimensional container), it's left behind in your original space.

**Source:** `= this.source` (`= this.source-type`)
