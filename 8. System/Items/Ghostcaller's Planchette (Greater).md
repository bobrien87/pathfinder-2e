---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 21000}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This miniature wooden planchette is engraved with symbols designed to attract spirits. When affixed, the symbols begin to glow, and the planchette turns slightly insubstantial. The spell DC of any spell cast by activating this item is 38.

- **Armor** After you cast a spell by activating the planchette, you gain resistance 10 to all physical damage (except [[Ghost Touch]]) until the start of your next turn. Attacks by incorporeal creatures (such as a ghost's ghostly hand) count as *ghost touch*.

> [!danger] Effect: Ghostcaller's Planchette   Armor

- **Weapon** After you cast a spell by activating the planchette, the affixed weapon gains the effects of both the *ghost touch* and Greater Vitalizing property runes until the end of your next turn.

> [!danger] Effect: Ghostcaller's Planchette   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Void Warp]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 7th-rank [[Invoke Spirits]]

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Tempest of Shades]]

**Source:** `= this.source` (`= this.source-type`)
