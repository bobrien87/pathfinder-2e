---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Elf]]", "[[Finesse]]", "[[Forceful]]"]
price: "{'gp': 4500}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The blade of this *+2 greater striking holy standard-grade cold iron elven curve blade* shines with a pale fire that illuminates the wielder's face in a grim visage and produces dim light in a @Template[type:emanation|distance:10]. The wielder can suppress or reactivate this light as a single action with the concentrate trait.

**Activate—Reveal Demons** `pf2:1` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You brandish *Morning Glow* and focus on its gleaming light, boosting its illumination so that it produces bright light in a @Template[type:emanation|distance:30] (and dim light for another 30 feet) for 10 minutes. All creatures in this area that have the demon trait must attempt a DC 31 [[Reflex]] save.

> [!danger] Effect: Morning Glow
- **Success** The demon is unaffected by the glow.
- **Failure** The demon becomes outlined with a shimmering aura of dim light that causes it to become [[Dazzled]]. If the demon was [[Invisible]], it becomes [[Concealed]] instead. If it was already concealed for any other reason, it is no longer concealed. This light affects the demon for 1 minute.
- **Critical Failure** As failure, but with a duration of 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
