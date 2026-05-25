---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Camel"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +7, Survival +6"
abilityMods: ["+4", "+3", "+4", "-4", "+1", "-1"]
abilities_top:
  - name: "Desert-Adapted"
    desc: "A camel is well-adapted to heat and deserts. If allowed to drink and eat its fill, (roughly 40 gallons), it can [[Subsist]] for 2 weeks without needing to attempt Survival checks, and it treats environmental heat as if it was one step less severe."
  - name: "Camel Spit"
    desc: "To drive away enemies, the camel spits the partially digested contents of its stomach at a creature within 10 feet. <br>  <br> On a hit, the target is [[Dazzled]] for 1 round and must succeed at a DC 17 [[Fortitude]] save or become [[Sickened]] 1. <br>  <br> The camel can't use its camel spit Strike again for 1d4 rounds."
armorclass:
  - name: AC
    desc: "15; **Fort** +9, **Ref** +8, **Will** +4"
health:
  - name: HP
    desc: "20"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (unarmed), **Damage** 1d6+4 piercing"
  - name: "Ranged strike"
    desc: "Spit +6 (`pf2:1`), **Damage**  plus [[Camel Spit]]"
spellcasting: []
abilities_bot:
  - name: "Sand Stride"
    desc: "`pf2:2` The camel Strides twice. It has a +5-foot circumstance bonus to its Speed during these Strides, ignoring difficult terrain caused by rubble, sand, and uneven ground made of earth and stone."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

For generations untold, nomads and traders have relied on sure-footed camels to cross the harsh deserts and trackless wastes around the world. Thriving where other animals wither and perish, camels are well-adapted to their homes with tough skin and the ability to store nutrients within their bodies. Properly cared for, these "ships of the desert" can trek for weeks between oases without trouble.

Camels have three eyelids to protect them from desert sands and other blowing debris. One lid is completely clear, which allows them to see and travel during high winds. When sandstorms strike, camels completely close their nostrils to protect their lungs. Their underbellies also sport a thick, specialized skin, allowing them to lay down safely on burning hot sands.

Contrary to popular belief, fatty tissue comprises a camel's humps rather than water. This stored energy allows the animals to survive long distances between feedings. These herbivores can also readily digest hardy scrub brush inedible to other species, making them one of the hardiest desert survivors. Strong as a warhorse, camels can run fast and even sprint for short periods of time when they feel threatened, though they prefer a slow, plodding pace to conserve energy.

One-humped camels, also called dromedaries, are more common in the deserts of northern Garund, while the two-humped variety are native to the dry steppes of Casmaron. Both species have tall and lanky builds, standing about 6 feet at the shoulder and weighing around 2,000 pounds. They can be ornery when mishandled, and they don't hesitate to bite, kick, or even spit a noxious substance on riders who don't treat them well.

In addition to transporting people and goods, camels are a key source of fiber for clothing and tents as well as milk. Their meat is highly nutritious and surprisingly tasty, but given the creatures' utility, this use is reserved for special occasions or truly dire situations.

```statblock
creature: "Camel"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
