---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 6500}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The broken tips of four dragon claws—one of each magical tradition—are set into a silver fitting. They protrude in the shape of a star or compass.

- **Armor** After you cast a non-cantrip spell by activating the spindle, you gain resistance 10 to fire, force, mental, and spirit for 1 minute.
- **Weapon** After you cast a non-cantrip spell by activating the spindle, you gain a Dragon Breath activity that takes 2 actions and deals 9d6 damage to all creatures in a @Template[type:cone|distance:30] with a DC 34 [[Reflex]] save. Choose the type of damage when you use Dragon Breath: @Damage[9d6[fire]|options:area-damage]{fire}, @Damage[9d6[force]|options:area-damage]{force}, @Damage[9d6[mental]|options:area-damage]{mental}, or @Damage[9d6[spirit]|options:area-damage]{spirit}. You can use this activity once before the end of your next turn.

> [!danger] Effect: Wyrm Spindle   Armor

**Activate** Cast a Spell

**Effect** You cast [[Gouging Claw]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 7th-rank [[Summon Dragon]].

**Source:** `= this.source` (`= this.source-type`)
