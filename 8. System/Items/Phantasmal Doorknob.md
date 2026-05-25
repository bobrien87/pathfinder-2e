---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Emotion]]", "[[Magical]]", "[[Mental]]", "[[Spellheart]]"]
price: "{'gp': 215}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ornate doorknob can open doors both material and metaphysical, revealing dreams and nightmares. The spell DC of any spell cast by activating this item is 20.

- **Armor** You gain a +1 item bonus to Thievery checks to Pick a Lock.
- **Weapon** If you critically succeed at a Strike with the weapon, the target is [[Dazzled]] until the end of its next turn.

> [!danger] Effect: Phantasmal Doorknob   Armor

> [!danger] Effect: Phantasmal Doorknob   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Figment]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Phantasmal Treasure]].

**Source:** `= this.source` (`= this.source-type`)
