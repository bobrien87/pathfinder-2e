---
type: creature
group: ["Humanoid", "Samsaran"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Samsaran Anchorite"
level: "1"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Samsaran"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]]"
languages: "Common, Empyrean, Samsaran"
skills:
  - name: Skills
    desc: "Medicine +6, Occultism +6, Religion +7, Society +4"
abilityMods: ["+0", "+2", "+0", "+1", "+4", "+2"]
abilities_top:
  - name: "Cryptomnesia"
    desc: "A samsaran anchorite subconsciously retains bits of knowledge from their innumerable former lives, granting them a +1 circumstance bonus to skill checks that aren't listed in their skills above, and allowing them to attempt all skill actions that normally require the user to be trained."
armorclass:
  - name: AC
    desc: "15; **Fort** +3, **Ref** +7, **Will** +9"
health:
  - name: HP
    desc: "15"
abilities_mid:
  - name: "All This Has Happened Before"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The samsaran anchorite is about to roll initiative <br>  <br> **Effect** The anchorite experiences a flash of recognition from a previous existence, gaining a +4 circumstance bonus to the triggering roll. <br>  <br> If this causes the anchorite to be the first creature to act, they also become [[Quickened]] for 1 round, but they can use the extra action only to [[Recall Knowledge]] or Step."
  - name: "All This Will Happen Again"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The samsaran anchorite fails or critically fails a Will save against an emotion effect <br>  <br> **Effect** Even in the face of overwhelming tribulation, the anchorite finds solace in the notion that all things are merely part of a never-ending cycle.They reroll the saving throw with a +1 status bonus; they must use the second result."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spear +5 (`pf2:1`), **Damage** 1d6+2 piercing"
  - name: "Ranged strike"
    desc: "Sling +7 (`pf2:1`) (reload 1, range 50 ft.), **Damage** 1d4+2 bludgeoning"
spellcasting:
  - name: "Divine Prepared Spells"
    desc: "DC 17, attack +9<br>**1st** (3 slots) [[Command]], [[Heal]], [[Sanctuary]]<br>**Cantrips** [[Guidance]], [[Light]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A unique connection to the cycle of life and death defines the mortal lives of samsarans. With a tendency toward reclusiveness, samsarans have delicate builds, enigmatic and pupilless eyes, and blood as clear as water. When a samsaran dies, their body vanishes and their soul instantly reincarnates into a newborn child elsewhere on the same plane: usually another samsaran, but occasionally a humanoid of a different ancestry.

Though all samsarans have an innate understanding of their nature, they consciously remember little from their former lives. Some, however, are occasionally struck by disjointed memories or flashes of déjà vu linked to a previous existence that can earn them a reputation for preternatural wisdom and insight. Most samsarans prefer to lead studious lives filled with moments of deep reflection. Their sights remain set on the eternal and on enlightenment, reducing the appeal of the short-term material gains one can achieve in just one lifetime. A samsaran ceases their cycle of reincarnation only upon reaching perfect state of enlightenment-or falling so far from harmony that they proceed to a doomed afterlife.

The ancestral home of the samsarans lies in Zi Ha, a remote mountain nation in Tian Xia. These treacherous mountains help ensure the solitude most samsarans prefer, and they're further protected by misguiding illusions, defensive wards, and secure fortifications.

```statblock
creature: "Samsaran Anchorite"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
