---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Xoarian"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Thoughtsense]] (precise) 60 feet, [[Tremorsense]] (imprecise) 60 feet"
languages: "Aklo ((Can't Speak Any Languages), Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +14, Deception +20, Diplomacy +16, Occultism +17, Society +17, Stealth +18"
abilityMods: ["+2", "+4", "+4", "+5", "+4", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Stolen Identity"
    desc: "While a xoarian uses Body Thief, it gains the ability to understand and speak all languages known by the host, as well as knowledge of the host body's abilities, identity, role in society, and personality. However, it does not gain the specific memories or knowledge of the host body."
  - name: "Thoughtsense 60 feet"
    desc: "The xoarian senses a creature's mental essence as a precise sense with the listed range; it cannot sense mindless creatures with thoughtsense."
armorclass:
  - name: AC
    desc: "26; **Fort** +14, **Ref** +16, **Will** +18"
health:
  - name: HP
    desc: "130; **Immunities** blinded, controlled, emotion, possession"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tentacle +18 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d10+5 piercing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 27, attack +19<br>**4th** [[Confusion]], [[Dispelling Globe]]<br>**3rd** [[Paralyze]]<br>**2nd** [[Invisibility (At Will, Self Only)]], [[Paranoia]] (At Will)<br>**1st** [[Daze]], [[Detect Magic]], [[Read Aura]], [[Soothe]]"
abilities_bot:
  - name: "Body Thief"
    desc: "`pf2:3` The xoarian squeezes itself into the head of a creature dead no longer than a day, consuming and replacing that creature's brain. At the start of the xoarian's next turn, the body revives at its maximum Hit Points, controlled by the xoarian. The xoarian is conscious and can sense everything the possessed body could. Any effect that ends the possession kills the host body with the same effects as Exit Body. The xoarian can't use any of the host creature's spells with Body Thief but can use its own innate spells."
  - name: "Exit Body"
    desc: "`pf2:1` **Requirements** The xoarian is controlling a body with Body Thief <br>  <br> **Effect** The xoarian bursts out of its host body, which dies instantly and is no longer a suitable host for any Body Thief ability. The xoarian stretches to its full size in an adjacent space."
  - name: "Ravage"
    desc: "`pf2:3` The xoarian makes two tentacle Strikes against a single [[Paralyzed]], [[Restrained]], or [[Unconscious]] creature. If the target has 0 Hit Points after Ravage, the xoarian can use a free action with the death trait to kill the target and occupy it with Body Thief."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The five-tentacled xoarians infiltrate many societies, although it's unclear how much of their activities are at the behest of the Dominion of the Black and how much is for their own perverse enjoyment. Known as corpse riders by Golarion scholars, little is understood of their origins beyond the suspicion that they come from a distant planet named Xoar.

When a xoarian infiltrates a community, its first priority is to acquire a host body. They often choose the recently dead for this role, as murdering a living host could draw unwanted attention. When the aberration compresses itself into a host's brain cavity, it becomes able to move the host's body as its own. It also acquires a complex range of senses it normally lacks.

Each new body brings the opportunity for new tastes, sounds, sights, and even pains. When gathered in groups, xoarians work to increase their status and taste the experiences denied to the lower classes. Xoarians controlling a body have little to fear but discovery, and even that simply pauses their games. Harm to the host is just another sensation to experience, and replacement bodies are easy to find.

The Dominion of the Black is a conglomeration of deep-space conquerors with a strong presence on Aucturn, the most remote planet in Golarion's solar system. The Dominion has secret outposts all over Golarion; most of its members on the planet are scouts, using their skills to steal brains and identities, gathering information without any consideration for the inhabitants of the worlds they infiltrate.

```statblock
creature: "Xoarian"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
