---
type: creature
group: ["Agathion", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Draconal"
level: "20"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Agathion"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+36; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Diabolic, Draconic, Empyrean (Speak with animals, Truespeech)"
skills:
  - name: Skills
    desc: "Arcana +38, Crafting +30, Deception +35, Diplomacy +37, Intimidation +35, Medicine +34, Nature +34, Religion +36, Society +32, Survival +32, Nirvana Lore +36"
abilityMods: ["+10", "+5", "+8", "+8", "+10", "+9"]
abilities_top:
  - name: "Dragon's Wisdom"
    desc: "Draconals embody the core value of wisdom, and all wisdom is obtained through understanding. If a draconal successfully [[Recalls Knowledge]] about a creature, they learn their highest weakness in addition to any other obtained knowledge, and any spirit damage they do to that creature becomes damage of their highest known weakness instead."
armorclass:
  - name: AC
    desc: "45; **Fort** +34, **Ref** +31, **Will** +38"
health:
  - name: HP
    desc: "370"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +38 (`pf2:1`) (holy, magical, reach 15 ft.), **Damage** 4d6 spirit plus 3d12+18 piercing"
  - name: "Melee strike"
    desc: "Claw +38 (`pf2:1`) (agile, holy, magical, reach 10 ft.), **Damage** 3d8+18 slashing plus 4d6 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 46, attack +38<br>**10th** [[Manifestation]]<br>**9th** [[Implosion]], [[Wrathful Storm]]<br>**8th** [[Earthquake]]<br>**7th** [[Divine Decree]]<br>**6th** [[Truesight]] (Constant)<br>**5th** [[Breath of Life]], [[Truespeech]] (Constant)<br>**2nd** [[Dispel Magic]], [[Speak with Animals]] (Constant)<br>**1st** [[Heal]]"
  - name: "Champion Focus Spell"
    desc: "DC 46, attack +0<br>**1st** [[Lay on Hands]]"
abilities_bot:
  - name: "Breath of Wisdom"
    desc: "`pf2:2` The draconal breathes a blast of energy that deals @Damage[21d6[spirit]|options:area-damage] damage to creatures they choose to damage in a @Template[type:cone|distance:60] (DC 44 [[Reflex]] save). They can make this efect nonlethal for selected creatures in the area or choose not to damage certain creatures at all. They can't use Breath of Wisdom again for 1d4 rounds."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Dragon agathions, known as draconals, number among the most powerful of their kin and also the wisest, embodying the wisdom of a benevolent philosopher-king. With their wisdom comes an elevation above material matters, making them the most removed from the troubles and lives of mortals. Draconals serve as the guardians of powerful magic, and they dispense their wisdom in service of the greater good of Nirvana and the celestial planes.

As celestial beings, draconals are opposed to unholy and wicked forces. They're patient and ageless creatures, and their machinations against the forces of evil sometimes move at a glacial pace. Draconals tend to have more immediate and direct impact working as mentors to mortals. They can provide counsel and knowledge to individuals or groups of heroes working against wickedness, guiding the mortals to excise evil with scalpel-like precision. This mentorship also allows a draconal to maintain their focus on planar matters or a larger, long-term plan against evil. Some draconals see the presence of evil as something useful, a motivation to stir benevolent creatures into action. To mortals, this outlook can sometimes appear as indifference, but draconals rarely knowingly allow an evil to grow out of hand.

Draconals appear more draconic than humanoid. They walk on their hind legs and balance on their long, serpent-like tails. Sharp claws tip their scaled humanoid hands. Each draconal often embodies a core wisdom of some kind. This wisdom often affects their physical appearance in distinct ways. For example, a draconal who believes the greatest wisdom is in understanding yourself will likely have refective scales, allowing those who look upon them to see themselves fully. Because of this, draconals come in all different shapes, sizes, and colors.

```statblock
creature: "Draconal"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
