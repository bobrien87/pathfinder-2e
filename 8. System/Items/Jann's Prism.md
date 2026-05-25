---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Light always seems to be refracting through this simple prism, creating a hazy multicolor aura that surrounds the glass. When exposed to direct sunlight, the prism radiates a beam of light that shifts in color. This beam spells out the name of the jann shuyookh for whom the prism was designed. While holding the prism to your eye, your vision becomes overwhelmed with colors that guide your eye, granting you a +2 item bonus to visual Perception checks. If you look through the prism while you [[Seek]], you can scan or search an area twice as large as normal (a @Template[cone|distance:60], @Template[burst|distance:30], or @Template[square|distance:20]) as the varying colors help you distinguish between your surroundings.

**Activate - Jann's Light** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You raise the prism above your head and call upon the jann shuyookh to come to your aid. The shuyookh's face becomes visible in a reflection in the prism and light shines out from the prism, surrounding you in a multitude of colors. For 1 minute, you shed bright light in a @Template[emanation|distance:20] (and dim light for the next 20 feet). The light coruscates with two colors chosen by the jann, and you gain resistance 5 to two damage types based on the colors chosen: **red** fire, **orange** acid, **yellow** electricity, **green** poison, **blue** sonic, **indigo** mental, or **violet** force.

> [!danger] Effect: Jann's Prism (Jann's Light)

**Source:** `= this.source` (`= this.source-type`)
