---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Censer]]", "[[Fire]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The *brazier of harmony* is a circular, orb-shaped censer etched with celebrating creatures shaking hands and dancing. The brazier contains a pleasant-smelling potpourri of dried flowers and incenses, designed to create a calm atmosphere that encourages meditation, thoughtfulness, and camaraderie. While holding the lit censer, you gain a +1 item bonus to Diplomacy checks, whether the censer is activated or not.

**Activate—Light Incense** `pf2:2` (aura, manipulate)

**Frequency** once per day

**Cost** incense worth at least 1 sp

**Effect** When the incense is lit, pleasant, floral smoke surrounds the censer in a @Template[emanation|distance:20], creating a space of peace and harmony. Each creature that breathes the smoke is affected by 3rd-rank [[Calm]] and is then temporarily immune for 24 hours. The spell's effects end when the incense burns out.

**Source:** `= this.source` (`= this.source-type`)
