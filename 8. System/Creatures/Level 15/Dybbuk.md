---
type: creature
group: ["Incorporeal", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dybbuk"
level: "15"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Spirit"
trait_03: "Undead"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]]"
languages: "Aklo, Chthonian, Common (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +28, Deception +31, Diplomacy +27, Intimidation +29, Stealth +28"
abilityMods: ["-5", "+7", "+0", "+1", "+6", "+8"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
armorclass:
  - name: AC
    desc: "35; **Fort** +21, **Ref** +28, **Will** +29"
health:
  - name: HP
    desc: "175; void healing; **Immunities** death effects, disease, paralyzed, poison, precision, unconscious, bleed; **Resistances** all damage 10 except force, ghost touch, spirit, vitality"
abilities_mid:
  - name: "Frightful Presence"
    desc: "30 feet. DC 33 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ghostly Hand +28 (`pf2:1`) (agile, finesse, magical, unholy), **Damage** 3d10+14 void plus 2d6 spirit"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 36, attack +30<br>**6th** [[Dominate]], [[Never Mind]]<br>**4th** [[Rewrite Memory]]<br>**3rd** [[Chilling Darkness]]<br>**2nd** [[Telekinetic Maneuver]] (At Will)<br>**1st** [[Fear]], [[Fear]] (At Will), [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Malevolent Possession"
    desc: "`pf2:2` The dybbuk attempts to possess an adjacent corporeal creature. This has the same effect as the [[Possession]] spell (DC 34 [[Will]] save) with an unlimited duration, except since the dybbuk doesn't have a physical body, they aren't [[Unconscious]], and aren't [[Paralyzed]] when the effect ends, though they take 5d6 spirit damage if the body is knocked unconscious or killed. <br>  <br> If the dybbuk took control of the target with Malevolent Possession, when the dybbuk departs, the target has only incoherent memories of the interval it was possessed."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The discorporated spirits called dybbuks arise from souls denied respite in the afterlife, often because they committed some great transgression in life. These spirits are said to cling to life through possessing victims to escape the punishment awaiting them in the afterlife. Only by trapping, cowing, or destroying such spirits can a mortal hope to drive them back.

Dybbuks, who are most often the spirits of men, hide within possessed victims. Their targets of possession are usually young women on the eve of their wedding nights, which can be seen as an omen of an ill-fitting match, particularly in arranged marriages. Male and nonbinary victims do exist as well, though in lesser quantities, and also often on the eve of a troubled marriage. No one knows for sure why dybbuks are drawn to such situations, though it may be because the transgressive soul of a dybbuk seeks to bring chaos to the most strictly regimented aspects of society.

A victim possessed by a dybbuk might be loud and crude, refuse to eat or drink, perform profane acts, or otherwise stir up trouble in the victim's household. The possessed victim has no memory of these events after their possession ends.

Certain classes of specially trained priests can expel dybbuks from their victims through exorcism. Typically, this uses a methodology combining smoke, the blowing of a horn from a ram, and the recitation of holy verses. Exorcisms are, however, extremely difficult and dangerous, and require great knowledge and skill on the part of the priest due to the power of these malevolent spirits.

```statblock
creature: "Dybbuk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
