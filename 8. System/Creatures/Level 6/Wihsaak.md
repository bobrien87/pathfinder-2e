---
type: creature
group: ["Fiend", "Sahkil"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wihsaak"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Chthonian, Diabolic, Empyrean, Requian (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Deception +15, Intimidation +15, Stealth +15"
abilityMods: ["+4", "+5", "+4", "+1", "+2", "+3"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Easy to Call"
    desc: "A wihsaak's level is considered 2 lower for the purpose of being conjured by the [[Binding Circle]] ritual (and potentially other rituals, at the GM's discretion), but it is always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
armorclass:
  - name: AC
    desc: "24; **Fort** +14, **Ref** +15, **Will** +14"
health:
  - name: HP
    desc: "105; **Immunities** fear effects; **Weaknesses** holy 5"
abilities_mid:
  - name: "Swarmwalker"
    desc: "Swarms of animals and other unintelligent creatures instinctively leave a wihsaak alone. A wihsaak is immune to the damage from and effects of swarms with an Intelligence of –5."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +17 (`pf2:1`) (finesse, unarmed, unholy), **Damage** 2d10+7 slashing plus 1d4 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +15<br>**4th** [[Suggestion]]<br>**2nd** [[Blur]], [[See the Unseen]], [[Vomit Swarm]]<br>**1st** [[Detect Magic]], [[Fear]]"
abilities_bot:
  - name: "Droning Distraction"
    desc: "`pf2:1` **Effect** The wihsaak beats its wings rapidly, creating a buzzing drone that numbs creatures' minds. Each creature within @Template[emanation|distance:100]{100 feet} must attempt a DC 23 [[Will]] save. They are then temporarily immune for 1 minute. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Confused]] and [[Stupefied 1]] for 1 round. <br> - **Critical Failure** The creature is confused for 1 round and [[Stupefied 2]] for 1 minute."
  - name: "Skip Between"
    desc: "`pf2:1` The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These gaunt and insectile sahkils torment their foes by focusing on a widespread fear of insects and creeping, crawling vermin. Unlike their more subtle cousins, wihsaaks don't lurk in the periphery and instead directly engage their targets, using their unnerving buzzing to disorient and terrify.

When encountering multiple foes, wihsaaks attempt to spread fear to everyone before slashing at them with their devastating claws.

Ages ago, when this cycle of the multiverse was still adolescent, a cabal of psychopomps who already felt bored and restrained in their role of ushering souls to their ultimate resting place rebelled against their station. It was this corruption of the cycle of souls that spawned the first sahkils.

Ambivalent to the prescribed order of the multiverse and spiteful of mortals, sahkils delight in spreading fear and unease to all beings, clogging up the metaphysical cycle with anxiety-ridden mortals too scared to achieve their potential. These fiends have drastically changed from their dedicated psychopomp predecessors. They are creatures of spite and torment, fear and disgust. They exploit the most common and rare fears for their own perverse satisfaction, and they want nothing more than to frighten mortals and make them quetion their reason for existence.

Most sahkils lurk on the Ethereal Plane, but they frequently invade the Material Plane to torment mortals and spread terror. They use their innate ability to slip between the veils of the Ethereal and Material effortlessly, often stalking their targets for days or weeks before enacting their devious plots.

```statblock
creature: "Wihsaak"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
