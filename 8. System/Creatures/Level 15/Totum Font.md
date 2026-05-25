---
type: creature
group: ["Air", "Earth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Totum Font"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Air"
trait_02: "Earth"
trait_03: "Elemental"
trait_04: "Fire"
trait_05: "Metal"
trait_06: "Water"
trait_07: "Wood"
perception:
  - name: Perception
    desc: "+30; [[Darkvision]]"
languages: "Muan, Petran, Pyric, Sussuran, Talican, Thalassic (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +25, Arcana +30, Athletics +29, Crafting +30, Nature +31, Elemental Lore +33"
abilityMods: ["+6", "+3", "+4", "+8", "+3", "+3"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "35 37 with shield raised, all-around vision; **Fort** +26, **Ref** +23, **Will** +29"
health:
  - name: HP
    desc: "104"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Elemental Attunement"
    desc: "A totum font is always attuned to a single element (air, earth, fire, metal, water, or wood), represented by which of their faces points forward. They can change this attunement to the element of their choice as a single action, or as a free action when they roll initiative."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Requirements** The font is attuned to air, fire, or water. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Shield Block"
    desc: "`pf2:r` **Requirements** The font is attuned to earth, metal, or wood. <br>  <br> **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tendril +30 (`pf2:1`) (magical, reach 10 ft.), **Damage** 3d8+16 bludgeoning"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 33, attack +25<br>**5th** [[Truespeech]] (Constant)"
abilities_bot:
  - name: "Briar's Hold"
    desc: "`pf2:2` **Requirements** The font is attuned to wood <br>  <br> **Effect** Each creature within 20 feet must succeed at a DC 36 [[Fortitude]] save or become [[Slowed]] 1 for 1 minute. When a creature already slowed by Briar's Hold fails its Fortitude save, it becomes [[Petrified]] for 1 minute but is turned to wood instead of stone."
  - name: "Brilliance of Flame"
    desc: "`pf2:2` **Requirements** The font is attuned to fire <br>  <br> **Effect** The font flies 30 feet and explodes in a fiery Elemental Eruption."
  - name: "Elemental Eruption"
    desc: "`pf2:2` The font explodes in a cacophony of color and energy. Each creature in a @Template[type:emanation|distance:20] takes @Damage[9d6[bludgeoning]|options:area-damage] damage (DC 36 [[Reflex]] save). The explosion deals bludgeoning damage unless the font is attuned to air (electricity damage), fire (fire damage), metal (slashing damage), or wood (piercing damage). Elemental Eruption gains the trait matching the element the font is attuned to."
  - name: "Entomb"
    desc: "`pf2:0` **Requirements** The font is attuned to earth, and its last action was a successful tendril Strike <br>  <br> **Effect** The font attempts an Athletics check to [[Grapple]] the target of the Strike."
  - name: "Overflowing Tide"
    desc: "`pf2:2` **Requirements** The font is attuned to water <br>  <br> **Effect** Elemental waves surge around the font, creating a torrential Elemental Eruption and pushing creatures in the area 20 feet (or 10 feet on a successful saving throw)."
  - name: "Serrated Flurry"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The font is attuned to metal <br>  <br> **Effect** The font lashes out with two tendril Strikes, each targeting a different creature within their reach. These Strikes deal slashing damage."
  - name: "Tempest Charge"
    desc: "`pf2:1` **Requirements** The font is attuned to air <br>  <br> **Effect** The font Flies 60 feet and makes a tendril Strike against a creature it hasn't attacked this turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Before mortals, fey, or even genies, totum fonts were the first creatures born of six elements undivided and harmonious. From the fonts sprung new elemental children, and they aided the gods in the many acts of creation that would follow.

Wellsprings of OneWithout access to the balance of all six elemental planes, a totum font becomes fractured and inundated in a single element. Most were healed when the Planes of Metal and Wood returned, but some of these so-called "wellsprings of one" still wander the universe, agitated and confused.

```statblock
creature: "Totum Font"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
