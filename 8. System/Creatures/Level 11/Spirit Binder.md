---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spirit Binder"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+20; [[Spiritsense]] (imprecise) 60 feet"
languages: "Common, Necril, Shadowtongue"
skills:
  - name: Skills
    desc: "Diplomacy +21, Intimidation +21, Occultism +22, Spirits Lore +24"
abilityMods: ["+1", "+3", "+3", "+5", "+4", "+6"]
abilities_top:
  - name: "Spiritsense"
    desc: "The spirit binder can sense the spirits of creatures, including living creatures, most non-mindless undead, and haunts within the listed range. Since spiritsense detects spiritual essence, not physical bodies, it can detect spirits projected by spells (such as [[Project Image]]) or possessing otherwise soulless objects. It can't detect soulless bodies, constructs, or objects, and like most senses, it doesn't penetrate through solid objects."
  - name: "Spirit Scrying"
    desc: "The spirit binder's scrying spells can target or detect spirits on other planes as though the spirits were in the Universe."
armorclass:
  - name: AC
    desc: "28; **Fort** +19, **Ref** +19, **Will** +24"
health:
  - name: HP
    desc: "175"
abilities_mid:
  - name: "Haunting Spirits"
    desc: "30 feet. The spirits bound by a spirit binder swirl around, lashing out at their foes. An enemy that enters or starts its turn in the aura must succeed at a DC 27 [[Will]] save or take @Damage[3d6[spirit]|options:area-damage] damage and be [[Frightened]] 1 (double damage and [[Frightened]] 2 on a critical failure)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Ghost Claw +19 (`pf2:1`) (finesse, magical, spirit, unarmed), **Damage** 2d10+6 slashing plus 2d6 spirit"
  - name: "Ranged strike"
    desc: "Spirit Pitch +19 (`pf2:1`) (magical, spirit, range 60 ft.), **Damage** 2d6 spirit plus 3d6 spirit"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 31, attack +23<br>**7th** (3 slots) [[Interplanar Teleport (to or from the Ethereal Plane only)]]<br>**6th** (2 slots) [[Dominate]], [[Spirit Blast]]<br>**5th** (3 slots) [[Invoke Spirits]], [[Spiritual Guardian]], [[Wave of Despair]]<br>**4th** (3 slots) [[Clairvoyance]], [[Fly]], [[Talking Corpse]]<br>**3rd** (3 slots) [[Clairaudience]], [[Ghostly Weapon]], [[Levitate]]<br>**2nd** (3 slots) [[Darkness]], [[Ghostly Carrier]], [[Peaceful Rest]]<br>**1st** (3 slots) [[Bane]], [[Command]], [[Detect Magic]], [[Fear]], [[Figment]], [[Telekinetic Hand]], [[Telekinetic Projectile]], [[Void Warp]]"
abilities_bot:
  - name: "Succumb to the Void"
    desc: "`pf2:1` The spirit binder taps into the more nefarious spirits of the Void, becoming something morbid and cruel. For 1d4 rounds, their resistance, aura of spirits, Strikes, and spirit spells change their damage type from spirit damage to void damage and replace their spirit trait with the void trait."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Ghosts and other spirits swirl around the spirit binder, creating a constant aura of flickering faces and forms.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Spirit Binder"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
