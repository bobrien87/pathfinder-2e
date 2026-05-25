---
type: creature
group: ["Dragon", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ravener Husk"
level: "14"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Dragon"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +22, Athletics +28"
abilityMods: ["+8", "+0", "+6", "-5", "+4", "+4"]
abilities_top:
  - name: "Soulsense 60 Feet"
    desc: "A ravener senses the spiritual essence of living and undead creatures within the listed range. Creatures whose material bodies are one unit with their souls, like celestials and fiends, appear brighter to this sense."
armorclass:
  - name: AC
    desc: "35; **Fort** +28, **Ref** +22, **Will** +26"
health:
  - name: HP
    desc: "325; **Immunities** bleed, death effects, disease, paralyzed, poison, sleep; **Weaknesses** holy 10"
abilities_mid:
  - name: "Boneshatter"
    desc: "`pf2:r` **Trigger** The ravener husk takes any amount of bludgeoning damage <br>  <br> **Effect** The ravener's brittle bones shatter, spraying bone shards everywhere. Every creature within a @Template[type:emanation|distance:10] of the ravener husk takes @Damage[7d6[piercing]|options:area-damage] damage (DC 31 [[Reflex]] save)."
  - name: "Frightful Presence"
    desc: "90 feet. DC 31 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +29 (`pf2:1`) (agile, magical, reach 10 ft.), **Damage** 3d4+16 slashing plus 2d6 void"
  - name: "Melee strike"
    desc: "Jaws +29 (`pf2:1`) (magical, reach 15 ft.), **Damage** 3d8+16 piercing plus 2d6 void"
spellcasting: []
abilities_bot:
  - name: "Ravenous Repast"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Effect** The ravener husk makes a jaws Strike against a deceased creature that has been dead no longer than 1 minute, was holy, and was at least level 15 in life. The ravener attempts a DC 5 flat check; if successful, they transform back into a ravener with 1 Hit Point in their soul ward."
  - name: "Void Breath"
    desc: "`pf2:2` The ravener husk breathes a torrent of void energy that deals @Damage[16d6[void]|options:area-damage] damage in a @Template[type:cone|distance:40] (DC 34 [[Reflex]] save). They can't use Void Breath again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Raveners require a steady diet of souls, and a ravener that's unable to feed for too long eventually cannibalizes their own soul. Should a ravener's soul ward ever be reduced to 0 Hit Points by hunger while the ravener has more than 1 Hit Point (see Soul Ward) they lose all traces of their former identity (losing most of its unique traits, including the one matching its former tradition) and descend into a feral, nearly mindless state. Even if a ravener husk later consumes soul energy, the transformation can be reversed only via Ravenous Repast.

Though their lifespans can measure in millennia, all dragons must eventually perish. While many do so on the blades or under the spells of dragonslayers, some manage to outlast their enemies and must, in time, face the truth that awaits all living creatures at the end of their natural life span. As with many other creatures, some dragons respond to such looming reminders of their own mortality poorly, and the particularly prideful or wrathful of their kind often lash out in anger when confronted by this grim truth. Peace and acceptance are found by some dragons, but the most stubborn of their ilk (and invariably the most wicked) can pursue a different answer to the problem. These dragons seek out sinister rites that can transform them into undead creatures known as raveners.

A ravener's flesh is stripped away as part of the transformation, leaving only bones. What they lose in flesh, however, the dragon gains in soul-rending power, as their spiritual energy forms a protective barrier around their body, keeping it intact and allowing flight with now-skeletal wings. This existence isn't as easy to maintain as other forms of undeath, however, and the ravener must feed regularly on living souls to power their profane metabolism. Their hunger is much greater than that of a living dragon, so raveners are forced to relocate regularly, traveling to fresh hunting grounds each time they strip their current home of prey.

```statblock
creature: "Ravener Husk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
