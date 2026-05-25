---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Urglid"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Darkvision]], [[Tremorsense]] (imprecise) 60 feet, [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Common, Draconic, Empyrean, Necril (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Athletics +27, Crafting +24, Deception +22, Intimidation +27, Religion +24, Society +22, Stealth +27, Outer Rifts Lore +24"
abilityMods: ["+9", "+4", "+8", "+4", "+3", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Consecration Vulnerability"
    desc: "Dedicated to the desecration of graves, an urglid takes @Damage[(3d6+6)[mental]] damage each round they're within the area of an effect with the consecration trait. In addition, the demon's weakness to holy increases to 30 for 1 round the first time they take damage from [[Holy Water]] each turn. <br>  <br> > [!danger] Effect: Consecration Vulnerability"
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Earth Glide"
    desc: "The urglid can [[Burrow]] through any earthen matter, including rock. When they do so, the urglid moves at their full burrow Speed, leaving no tunnels or signs of its passing unless they choose to do so."
armorclass:
  - name: AC
    desc: "31; **Fort** +26, **Ref** +20, **Will** +20"
health:
  - name: HP
    desc: "290; **Weaknesses** cold iron 10, holy 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +25 (`pf2:1`) (agile, deadly 2d10, magical, reach 10 ft., unarmed, unholy), **Damage** 3d10+16 slashing"
  - name: "Melee strike"
    desc: "Leg +25 (`pf2:1`) (agile, magical, reach 15 ft., unholy), **Damage** 3d12+21 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22<br>**8th** [[Earthquake]]<br>**6th** [[Truesight]] (Constant)<br>**5th** [[Magic Passage]] (At Will), [[Wall of Stone]]<br>**3rd** [[Earthbind]] (At Will)"
abilities_bot:
  - name: "Gravechoke"
    desc: "`pf2:2` The urglid emits a putrid pulse that targets all living creatures within a @Template[emanation|distance:30]. Creatures in this area that fail a DC 30 [[Fortitude]] save become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure)."
  - name: "Ravenous Earthunholy"
    desc: "`pf2:1` With a single, devious thought, the urglid causes a mound of grave soil to well up at a creature's feet. That creature must succeed at a DC 30 [[Reflex]] save or become [[Restrained]] (`act escape dc=30`). The restrained creature then begins sinking below the ground into a spontaneously formed grave. A creature restrained by this ability for 3 rounds is buried 6 feet deep in the ground and begins suffocating within 1 minute. A buried creature must be dug up to be freed (see Burial on page 96 of GM Core). A creature that is slain by Ravenous Earth rises as a [[Ghoul]] the next midnight."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The hulking monstrosities known as urglids form from the souls of murderous undertakers, sadists who buried their victims alive, and intentionally neglectful grave keepers who gave up their watch over the dead. They seek to perpetuate their mortal sins as demons and use their fiendish powers to subject mortals to the terrors of vivisepulture. Other urglids find grave sites repulsive and will often destroy headstones and other grave markers. Without such markers, these graves are often lost and forgotten, a detail that pleases an urglid. Standing over 12 feet tall and weighing over 3,000 pounds, the demon has a head that seems sunken into their torso, and a gaping, toothy mouth that opens at the top of their chest.

```statblock
creature: "Urglid"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
