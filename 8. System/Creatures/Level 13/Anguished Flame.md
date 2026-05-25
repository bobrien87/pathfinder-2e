---
type: creature
group: ["Elemental", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Anguished Flame"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Elemental"
trait_02: "Fire"
trait_03: "Light"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28"
languages: "Empyrean, Pyric (Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +24, Crafting +27, Diplomacy +27, Medicine +27, Nature +23, Religion +23, Deity Lore (any one god) +25"
abilityMods: ["+5", "+7", "+5", "+4", "+6", "+8"]
abilities_top:
  - name: "Eternal Luminosity"
    desc: "An anguished fame naturally sheds brilliant light like a torch. When other creatures target the anguished fame, they ignore the [[Concealed]] condition from darkness, fog, mist, and smoke."
  - name: "Purifying Flame"
    desc: "An anguished fame can [[Treat Wounds]] without a healer's toolkit, instead healing the wounded with the gentle light of their touch."
armorclass:
  - name: AC
    desc: "33; **Fort** +22, **Ref** +24, **Will** +25"
health:
  - name: HP
    desc: "260"
abilities_mid:
  - name: "Solar Flare"
    desc: "30 feet. When a creature ends its turn in the aura, it takes @Damage[2d6[fire]|options:area-damage] damage (DC 33 [[Fortitude]] save). On a failed save, it also becomes [[Dazzled]] until the end of its next turn. The anguished fame can activate or deactivate this aura by using a single action with the concentrate trait."
  - name: "Vulnerable to Blasphemy"
    desc: "If a creature the anguished fame can see and hear spends 1 action with the linguistic trait blaspheming against the gods, the anguished fame becomes [[Sickened]] 1 until they Collect a Prayer from that creature."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Flaming Wing +25 (`pf2:1`) (agile, fire), **Damage** 3d10+11 fire"
  - name: "Ranged strike"
    desc: "Shining Ray +27 (`pf2:1`) (fire, light, range 60 ft.), **Damage** 3d6 spirit plus 3d6+6 fire"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22<br>**7th** [[Interplanar Teleport]]<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Fireball]]<br>**1st** [[Detect Magic]], [[Ignition]], [[Light]]"
abilities_bot:
  - name: "Collect Prayer"
    desc: "`pf2:2` The anguished fame compels a creature they can see within 60 feet, who must attempt a DC 30 [[Will]] save. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature immediately uses its reaction to pray. <br> - **Failure** The creature prays. It is [[Slowed]] 1 and can't use reactions for 1 minute. <br> - **Critical Failure** As failure, but the creature is [[Slowed]] 2."
  - name: "Focus Gaze"
    desc: "`pf2:1` **Requirements** The anguished fame's solar fare aura is active <br>  <br> **Effect** The anguished fame fixes their fery eyes on a creature they can see within 30 feet. The target must immediately attempt a Fortitude save against the anguished fame's solar fare. If the creature was already [[Dazzled]] by solar fare before attempting its save, a failed save causes it to become [[Blinded]] until the end of its next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Ancient tales tell that the elemental lord Atreia created his six-winged children to steward mortal prayers into the realms of the divine. These elementals work hand-in-hand with celestial and fendish deifc servants to accept sacrifces and offerings, but they also bless contrite mortals with absolution and purifcation, helping them to change the fate that awaits them after death.

```statblock
creature: "Anguished Flame"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
