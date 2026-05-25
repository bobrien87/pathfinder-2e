---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Deadly d8]]", "[[Disarm]]", "[[Finesse]]", "[[Magical]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The tip of this *+2 greater striking brilliant standard-grade cold iron rapier* shines with a flickering sheen of green light that mimics the glittering appearance of Castrovel in the night sky. The carrier of *Castrovel's Beacon* instinctively knows Castrovel's position in the sky even if it hasn't actually yet risen into view, which grants the wielder a +2 item bonus to [[Sense Direction]] when using the stars to orient themself. Additionally, the weapon grants a +2 item bonus to all saving throws against effects that cause the [[Dazzled]] or [[Blinded]] conditions.

When its *brilliant* rune is activated, the counteract rank is 6 and the counteract modifier is +21.

**Activate—Starlight Burst** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You cast [[Vibrant Pattern]] from *Castrovel's Beacon* as a 6th-rank arcane spell with a DC 31 [[Will]] save. Creatures with the elf trait are immune to Starlight Burst, and creatures with the demon trait take a –2 item penalty on all Will saves against the effect.

**Source:** `= this.source` (`= this.source-type`)
