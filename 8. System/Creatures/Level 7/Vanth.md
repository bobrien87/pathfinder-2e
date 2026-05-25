---
type: creature
group: ["Monitor", "Psychopomp"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Vanth"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Requian"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +17, Intimidation +15, Occultism +13, Religion +13, Stealth +17, Boneyard Lore +15"
abilityMods: ["+6", "+4", "+2", "+2", "+4", "+2"]
abilities_top:
  - name: "Infuse Weapon"
    desc: "A vanth's scythe is its symbol of office and gains a measure of its personal power. This scythe becomes a *+1 scythe* and is treated as if it were adamantine while the vanth wields it. A vanth whose scythe is taken or destroyed can infuse a new one with an hour of work."
  - name: "Shepherd's Touch"
    desc: "A vanth's Strikes affect incorporeal creatures with the effects of a *[[Ghost Touch]]* property rune and deal 2d6 void damage to living creatures and 2d6 vitality damage to undead."
armorclass:
  - name: AC
    desc: "27; **Fort** +15, **Ref** +13, **Will** +17"
health:
  - name: HP
    desc: "105; **Immunities** death effects, disease; **Resistances** void 10, poison 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Frightful Presence"
    desc: "20 feet. DC 22 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scythe +18 (`pf2:1`) (deadly d10, magical, trip), **Damage** 1d10+8 slashing plus [[Spirit Touch]]"
  - name: "Melee strike"
    desc: "Jaws +17 (`pf2:1`) (agile, unarmed), **Damage** 1d6+8 slashing plus [[Spirit Touch]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 22, attack +14<br>**4th** [[Translocate]], [[Translocate]] (At Will)<br>**3rd** [[Holy Light]], [[Locate]]<br>**2nd** [[Invisibility (At Will, Self Only)]]"
abilities_bot:
  - name: "Vanth's Curse"
    desc: "`pf2:2` **Frequency** three times per day <br>  <br> **Effect** The vanth bestows a curse on a creature by touching it with its scythe. The creature must attempt a DC 25 [[Will]] save. <br> - **Critical Success** The target is unaffected and is temporarily immune to Vanth's Curse for 24 hours. <br> - **Success** The target feels a momentary shudder of doom and is [[Stupefied 1]] for 1 minute by the distracting sensation. <br> - **Failure** The target becomes morose and glum as it accepts its own inevitable fate. For 1 hour, the target is [[Stupefied 2]]. Each time the target gains the dying condition, the stupefied condition value increases by 1, to a maximum value of [[Stupefied 4]]. <br> - **Critical Failure** As failure, but the effect is permanent."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Protectors of the Boneyard, the stern and resolute guardians of the dead, vanths are psychopomps who resemble skeletons with raven-like wings and a mask resembling a vulture's skull. Vanths carry black scythes to fight against those who would disturb the natural progression of souls, and they consider any visitor to the Boneyard a potential troublemaker. They rarely speak and even more rarely show any emotion other than a grim adherence to duty.

When the psychopomp armies go to war, vanths serve as front-line soldiers. In particular, daemons continually stage raids on the River of Souls, requiring constant patrol. Implacable warriors, vanths fly in perfect formation. This can backfire, as they often suppress any adaptability they possess as they wage war.

Psychopomps are guardians and shepherds of the dead in the Boneyard, the vast plane of graves where mortal souls are judged and sent on to their eternal rewards or damnations. Psychopomps ensure that the dead come to terms with their transition from mortality and are properly sorted into the appropriate afterlife. They also protect souls from being preyed upon by supernatural predators. Nearly all psychopomps wear masks, especially when they're likely to be interacting with mortals, although the types of masks they wear are as varied as the psychopomps themselves. The courts of the Boneyard preside in Requian, a somber yet melodic language spoken slowly with various tonal shifts.

Many psychopomps are intimately involved with the Boneyard's massive bureaucracy. Few pursue mercy, justice, or personal gain; their duties to Pharasma and her Boneyard are supreme. Nevertheless, individual psychopomps interpret their duties in different ways, which might put them in conflict with mortals or even with each other.

```statblock
creature: "Vanth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
