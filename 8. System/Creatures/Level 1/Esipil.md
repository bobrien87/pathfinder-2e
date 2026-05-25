---
type: creature
group: ["Fiend", "Sahkil"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Esipil"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Chthonian, Diabolic, Empyrean, Requian (Telepathy touch)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +6, Intimidation +7, Stealth +7"
abilityMods: ["+0", "+4", "+2", "+1", "+2", "+2"]
abilities_top:
  - name: "Telepathy (Touch)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Easy to Call"
    desc: "A esipil's level is considered 2 lower for the purpose of being conjured by the [[Binding Circle]] ritual (and potentially other rituals, at the GM's discretion), but it is always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "15; **Immunities** fear effects; **Weaknesses** holy 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +9 (`pf2:1`) (agile, finesse, unarmed, unholy), **Damage** 1d6 slashing plus 1d4 spirit"
  - name: "Melee strike"
    desc: "Jaws +9 (`pf2:1`) (finesse, magical, unholy, versatile p), **Damage** 1d4 spirit plus 1d8 slashing plus [[Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 15, attack +7<br>**2nd** [[Blur]]<br>**1st** [[Fear]], [[Fear]] (At Will), [[Telekinetic Hand]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The esipil transforms into a Tiny cat, dog, or other unassuming domestic animal. This doesn't affect the esipil's statistics, but it could change the damage type of its Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Skip Between"
    desc: "`pf2:1` The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Among the least of the sahkils, esipils delight in spreading fears and uncertainty among people who live with animals that could turn on them. They generally appear to their prey as some benign creature such as a domesticated dog or cat, but once they gain trust and get their victims close, they transform into a terrifying creature that looks part dog and part worm with tendrils of viscera that the creature uses as both a tongue and a weapon.

Of all the sahkils, esipils are most likely to ingratiate themselves with mortals, sometimes serving powerful spellcasters and other times simply living among unsuspecting victims, biding their time until they strike.

Ages ago, when this cycle of the multiverse was still adolescent, a cabal of psychopomps who already felt bored and restrained in their role of ushering souls to their ultimate resting place rebelled against their station. It was this corruption of the cycle of souls that spawned the first sahkils.

Ambivalent to the prescribed order of the multiverse and spiteful of mortals, sahkils delight in spreading fear and unease to all beings, clogging up the metaphysical cycle with anxiety-ridden mortals too scared to achieve their potential. These fiends have drastically changed from their dedicated psychopomp predecessors. They are creatures of spite and torment, fear and disgust. They exploit the most common and rare fears for their own perverse satisfaction, and they want nothing more than to frighten mortals and make them quetion their reason for existence.

Most sahkils lurk on the Ethereal Plane, but they frequently invade the Material Plane to torment mortals and spread terror. They use their innate ability to slip between the veils of the Ethereal and Material effortlessly, often stalking their targets for days or weeks before enacting their devious plots.

```statblock
creature: "Esipil"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
