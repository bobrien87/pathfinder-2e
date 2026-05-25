---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 400}"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** any

The body of a *weapon shot* is translucent and filled with quicksilver. It imparts its magic to the weapon used to fire it or it summons a translucent weapon, made of force, to fire it. It's a favorite of killers and sharpshooters who need just one shot in a situation where carrying ammunition is easier than carrying a weapon.

**Activate** `pf2:1` (concentrate)

**Effect** For the Strike with which you consume the ammunition, the weapon is a *+2 greater striking* weapon, instead of those of the weapon firing it.

**Activate** `pf2:2` (concentrate, manipulate)

**Effect** A ghostly weapon made of force appears, wielded by you and loaded with the *weapon shot* you activated. The conjured weapon sublimates into motes of briefly luminous dust if the *weapon shot* deactivates without you using it or just after you use the activated shot. For the Strike with which it functions, the weapon is a *+2 greater striking* weapon.

**Source:** `= this.source` (`= this.source-type`)
