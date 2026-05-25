---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 30}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Geometric precision and perfect angles signify that an artist with exemplary knowledge of dwarven tattooing traditions created this body art. Your family's ancestral stories, recited throughout the tattooing process, bind your blood even tighter to theirs. During your daily preparations, you manifest a visitation by an ancestor—possibly via a dream, a vision, or a magical trinket left by your bedroll. Roll `r 2d20` and record the highest result. Then roll `r 1d6` and note a type of saving throw: 1–2 Fortitude, 3–4 Reflex, and 5–6 Will.

> [!danger] Effect: Ancestral Geometry

In addition, until the next visitation, you gain a +1 item bonus to one Lore skill related to the ancestor, as determined by the GM. Usually, the ancestor provides a kind of knowledge they believe you'll need. For dwarven ancestors, the Lore skill is usually Architecture Lore, Engineering Lore, Genealogy Lore, Labor Lore, Mining Lore, Warfare Lore, or Lore about a dwarven deity.

**Activate** R (concentrate, fortune)

**Frequency** once per day

**Trigger** You rolled a saving throw of the noted type

**Effect** Replace the roll with the d20 roll from your ancestor's visitation.

**Source:** `= this.source` (`= this.source-type`)
