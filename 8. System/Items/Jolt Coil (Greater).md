---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Electricity]]", "[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 475}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Contained within this small glass tube is a twisted wire filament crackling with electricity, sending static prickling through the hair of anyone holding it. The spell DC of any spell cast by activating this item is 24.

- **Armor** You gain resistance 3 to electricity.
- **Weapon** After you cast an electricity spell by activating the coil, your Strikes with the weapon deal an additional 1d6 electricity damage until the end of your next turn.

> [!danger] Effect: Jolt Coil   Armor

> [!danger] Effect: Jolt Coil   Weapon

DC 24 [[Reflex]] save

**Activate** Cast a Spell

**Effect** You cast [[Electric Arc]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Lightning Bolt]].

**Source:** `= this.source` (`= this.source-type`)
