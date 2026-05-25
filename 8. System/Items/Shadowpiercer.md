---
type: item
source-type: "Remaster"
level: "23"
traits: ["[[Artifact]]", "[[Magical]]", "[[Monk]]", "[[Mythic]]", "[[Thrown 20]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Muted, silvery moonlight gleams along the curved blade of this *+4 major striking ghost touch spear*. Braided tassels of horsehair dangle from its sturdy haft, and archaic runes in Nidalese script shimmer along the weapon in the presence of shadow magic.

*Shadowpiercer* ignores immunity and resistance to precision damage of creatures with the incorporeal or shadow trait, and deals an additional 2d6 precision damage to such creatures. While wielding *Shadowpiercer*, you gain a +2 status bonus to saving throws against darkness and shadow effects; this bonus also applies to allies within 60 feet of you while you wield the spear. If you are a worshipper of [[Zon Kuthon]], you are [[Drained]] 4 and [[Enfeebled]] 4 while carrying or wielding *Shadowpiercer*. If you use a darkness or shadow effect while carrying or wielding *Shadowpiercer*, you become enfeebled 4; this condition's value reduces by 1 at the start of each day you do not have physical contact with *Shadowpiercer*.

**Activate—Absorb Shadows** `pf2:2` (concentrate, healing, manipulate, occult)

**Frequency** once per day

**Effect** You touch *Shadowpiercer* to a darkness or shadow effect to siphon its energy and bolster yourself. You gain a number of temporary Hit Points equal to four times the effect's counteract rank. These temporary Hit Points last for 1 hour. In addition, if the effect is causing darkness, that darkness is automatically counteracted within 15 feet of you for as long as you have those temporary Hit Points. This doesn't provide light—it merely restores the area to its natural illumination level.

**Activate—Rebuff Gloom** `pf2:r` (concentrate, occult)

**Trigger** You or an ally within 60 feet is targeted by a darkness or shadow effect

**Requirements** You don't currently have the drained condition

**Effect** Spend a Mythic Point; the spear drains your vitality to counteract the effect. You can attempt to counteract the effect (+46 modifier level, counteract rank 10). You can activate this effect without having a Mythic Point available but doing so makes you [[Drained]] 2.

**Destruction** *Shadowpiercer* simply disappears if a worshipper of Zon-Kuthon casts a 10th-rank [[Darkness]] spell on it once a day for an entire month while it is unattended.

**Source:** `= this.source` (`= this.source-type`)
