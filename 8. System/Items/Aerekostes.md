---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Divine]]", "[[Fatal d12]]", "[[Intelligent]]", "[[Mythic]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +16; precise vision 60 feet, imprecise hearing 60 feet

**Communication** telepathy

**Skills** Arcana +18, Religion +16

**Int** +6, **Wis** +4, **Cha** +3

**Will** +16

*Aerekostes* is a *+1 striking shifting falcata*. Though unable to move on their own, *Aerekostes* can flex, adjust their center of mass, and make other adjustments to adapt to a chosen wielder's fighting style. For the purposes of proficiency, class abilities, and feats (except those that would increase the weapon's damage die size), a wielder that *Aerekostes* approves of can treat *Aerekostes* as a martial weapon that belongs to their choice of the axe, brawling, club, knife, pick, spear, or sword weapon group. *Aerekostes* does not actually change form and their critical specialization effect does not change. As a hero-god, *Aerekostes* is a mythic being who starts each session with their own pool of 3 Mythic Points. Whenever their wielder would regain 2 or more Mythic Points, *Aerekostes* regains 1 Mythic Point.

**Activate—Forward Planning** `pf2:1` (concentrate, fortune)

**Frequency** once per minute

**Effect** *Aerekostes* studies the ongoing combat and myriad ways an upcoming attack might resolve. On the next attack made using *Aerekostes* before the end of their next turn, their wielder rolls twice and takes the better result.

**Activate—Spell Reserve** `pf2:1` (concentrate)

*Aerekostes* channels their mythic power into a minor miracle. They spend 1 Mythic Point, then casts one of the following as a 3rd-rank spell (DC 24 save as appropriate): [[Bane]], [[Bless]], [[Heroism]], [[Protection]], [[Resist Energy]], or [[Spiritual Armament]]. *Aerekostes* can use their actions to Sustain spells.

**Source:** `= this.source` (`= this.source-type`)
