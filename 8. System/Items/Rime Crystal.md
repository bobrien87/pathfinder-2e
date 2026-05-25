---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Cold]]", "[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 55}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Slowly spinning at the center of this crystalline orb is a single snowflake, and its surface remains lightly covered in frost no matter how hot the weather is outside. The spell attack modifier of any spell cast by activating this item is +7, and the spell DC is 17.

- **Armor** You gain resistance 2 to cold.
- **Weapon** After you cast a cold spell by activating the *crystal*, your Strikes with the weapon deal an additional 1d4 cold damage until the end of your next turn.

> [!danger] Effect: Rime Crystal   Armor

> [!danger] Effect: Rime Crystal   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Frostbite]].

**Source:** `= this.source` (`= this.source-type`)
