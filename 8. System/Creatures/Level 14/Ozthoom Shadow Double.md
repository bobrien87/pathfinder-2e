---
type: creature
group: ["Fey", "Summoned"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ozthoom Shadow Double"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fey"
trait_02: "Summoned"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Lifesense]] (precise) 120 feet, [[Low-Light Vision]]"
languages: "Aklo, Common, Fey (Can't speak any language, Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +28, Deception +25, Intimidation +27, Nature +22, Stealth +28"
abilityMods: ["+7", "+8", "+4", "+2", "+2", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Sneak Attack"
    desc: "A ozthoom shadow double's Strikes deal an additional 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "35; **Fort** +23, **Ref** +28, **Will** +24"
health:
  - name: HP
    desc: "85; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "Saving throws against Light effects"
    desc: "A shadow double that attempts a saving throw against a light effect can't get a result better than failure."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +25 (`pf2:1`) (agile, cold iron, unarmed), **Damage** 3d6+15 slashing"
  - name: "Melee strike"
    desc: "Wing +25 (`pf2:1`) (cold iron, reach 10 ft.), **Damage** 2d6+15 piercing plus 2d6 bleed"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Ozthooms are shadowy killers who serve powerful fey creatures or even the Eldest—the demigods of the First World. Amid the courts of the Eldest or other powerful fey rulers, these sinister assassins lurk overhead as they await the call to action—implied threats akin to deadly weapons hung as decor in a royal hall. Ozthooms never speak aloud; when they feel the need to communicate at all, they do so in a telepathic whisper directly into their victim's mind. While an ozthoom's body is a strange, fleshy material, their deadly claws and cruel hooked wings are made from razor-sharp cold iron, a quality that makes them highly feared among other fey. A typical ozthoom is 10 feet tall and has an 8-foot wingspan, but it weighs less than 80 pounds.

While most ozthooms serve powerful masters, a few of these murderous fey have been left to their own devices and serve none but their own capricious whims. In some cases, their master has been slain, while in others, the ozthoom has been released from service for any number of reasons. An ozthoom left to indulge their cruel desires unrestrained is often the most dangerous ozthoom of them all.

```statblock
creature: "Ozthoom Shadow Double"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
