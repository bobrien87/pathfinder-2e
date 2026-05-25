---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Reach]]", "[[Versatile s]]"]
price: "{'gp': 2}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder #221: Into the Apocalypse Archive"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +29; darkvision, imprecise hearing within 60 feet

**Communication** speech (Azlanti, Elven, Thassilonian)

**Skills** Arcana +33, Deception +29, Society +31

**Int** +8, **Wis** +6, **Cha** +4

**Will** +31

*Belimarius's Invidious Halberd* is a *+3 greater striking keen spell reservoir high-grade dawnsilver halberd* (at this time, their spell reservoir contains [[Slow]]). As the halberd passed from the hands of one runelord of envy to the next, the halberd's self-loathing and hatred of the arcane spellcasters they were forced to serve grew. Their own limited arcane magic paled in comparison to their powerful wielders, after all, and the halberd seethed at this perceived inequality. They only grudgingly abide their wielders—runelord or otherwise—and are only truly happy when they're used to cut down those who can cast arcane spells. The halberd can use 3 actions per turn, acting on their wielder's turn, and has a reaction. These actions and reaction don't count against their wielder's.

**Activate—Absorb Arcana** `pf2:r` (arcane, concentrate)

**Trigger** The halberd damages a creature capable of casting arcane spells

**Effect** The halberd attempts to absorb one of the creature's prepared arcane spells or arcane spell slots. If the creature struck fails a DC 37 [[Will]] save, it loses an arcane spell (or lose an unused arcane spell slot) as if it'd cast that spell. The spell or slot lost is randomly determined from the highest rank available, starting at 6th rank and working down. The halberd passes this absorbed energy on to their wielder, who becomes [[Quickened]] for 1 round and can use the extra action only to Strike with the halberd.

**Activate—Detonate Magic** `pf2:2` (arcane, concentrate)

**Frequency** once per day

**Effect** The halberd casts [[Detonate Magic]] (DC 37).

**Activate—Manipulate Mind** `pf2:2` (arcane, concentrate)

**Frequency** once per hour

**Effect** The halberd casts a 9th-rank [[Rewrite Memory]] (DC 37).

**Activate—Shattermind** `pf2:f` (arcane, concentrate)

**Trigger** The halberd critically hits a creature capable of casting arcane spells

**Effect** The creature struck is targeted with a 9th-rank [[Never Mind]] spell (DC 37).

**Destruction** *Belimarius's Invidious Halberd* is destroyed if it's hurled under the feet of the Oliphaunt of Jandelay while there's no current runelord of envy living in the world.

**Source:** `= this.source` (`= this.source-type`)
