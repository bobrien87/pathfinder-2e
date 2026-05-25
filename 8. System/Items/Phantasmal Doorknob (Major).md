---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Emotion]]", "[[Magical]]", "[[Mental]]", "[[Spellheart]]"]
price: "{'gp': 6000}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ornate doorknob can open doors both material and metaphysical, revealing dreams and nightmares. The spell DC of any spell cast by activating this item is 34.

- **Armor** You gain a +2 item bonus to Thievery checks to Pick a Lock.
- **Weapon** If you critically succeed at a Strike with the weapon, the target is [[Blinded]] until the end of its next turn. The creature is then temporarily immune to being blinded in this way for 24 hours.

> [!danger] Effect: Phantasmal Doorknob   Armor

> [!danger] Effect: Phantasmal Doorknob   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Figment]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 6th-rank [[Vision of Death]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Phantasmal Calamity]]

**Source:** `= this.source` (`= this.source-type`)
