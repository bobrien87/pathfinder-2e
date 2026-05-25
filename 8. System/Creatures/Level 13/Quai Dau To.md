---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Quai Dau To"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Darkvision]], [[Scent]] (imprecise) 120 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +27, Stealth +25, Survival +24"
abilityMods: ["+8", "+4", "+8", "-3", "+5", "-1"]
abilities_top:
  - name: "Mist Vision"
    desc: "The quai dau to ignores the [[Concealed]] condition from mist and fog."
armorclass:
  - name: AC
    desc: "32; **Fort** +26, **Ref** +19, **Will** +21"
health:
  - name: HP
    desc: "300; **Immunities** blinded, dazzled; **Weaknesses** sonic 15"
abilities_mid:
  - name: "Frightful Sight"
    desc: "60 feet. <br>  <br> This aura functions as a DC 32 [[Will]] save frightful presence aura, but a creature doesn't attempt its save until it sees the quai dau to. <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Reflective Scales"
    desc: "`pf2:r` **Trigger** A creature within 30 feet casts a spell with the light trait or uses an ability with the light trait <br>  <br> **Effect** The quai dau to adjusts its position to reflect the light off their scales in a blinding display. All creatures in a @Template[emanation|distance:30] must succeed at a DC 33 [[Fortitude]] save saving throw or become [[Blinded]] for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +27 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 3d12+14 piercing"
  - name: "Melee strike"
    desc: "Tail +27 (`pf2:1`) (reach 20 ft.), **Damage** 3d8+14 bludgeoning"
  - name: "Melee strike"
    desc: "Foot +27 (`pf2:1`) (agile, unarmed), **Damage** 3d8+14 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Drain Water"
    desc: "`pf2:1` **Requirements** The quai dau to is within 10 feet of a body of water that's at least 10 feet deep and their water sac is empty <br>  <br> **Effect** The quai dau to sucks water through their trunk to fill their water sac, lowering the level in the body of water by 10 feet. All creatures in the water within a @Template[emanation|distance:30] are [[Off Guard]] until the start of the quai dau to's next turn."
  - name: "Inflate"
    desc: "`pf2:1` The quai dau to inflates their body. They become Gargantuan, gain a fly Speed of 30 feet until the end of their next turn, and then Fly. They deflate if they fall [[Unconscious]] or Dismiss this effect."
  - name: "Mist Breath"
    desc: "`pf2:1` **Requirements** The quai dau to's water sac is full <br>  <br> **Effect** The quai dau to empties their water sac to breathe out mist in a @Template[emanation|distance:10]. All creatures within the mist become [[Concealed]], and all creatures outside the mist become concealed to creatures within it. The mist dissipates after 1 round."
  - name: "Spout Water"
    desc: "`pf2:2` **Requirements** The quai dau to's water sac is full <br>  <br> **Effect** The quai dau to empties its water sac to blast water from its trunk, dealing @Damage[9d10[bludgeoning]|options:area-damage] damage to all creatures in a @Template[line|distance:90], with a DC 33 [[Reflex]] save. A creature that fails is pushed 10 feet (or 20 feet on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

This big-headed beast is covered in glittering scales; its eyes are like large copper pots, and its mouth is full of sharp teeth. Despite its fish-like appearance, a quai dau to spends most of its time on land hunting along riversides or lakes. It uses its trunk to drain the nearby water before using it with deadly skill. A quai dau to can expel the water with a force strong enough to knock a knight off a horse, or gently enough to surround themself in a veil of mist.

A quai dau to is extremely sensitive to sound. If they hear too much ruckus near their hunting grounds, they violently attack. Their silent movement allows them to sneak up on such distracted prey despite their massive size. Researchers have discovered, after much study, that quai dau tos don't have ears in the traditional sense. They have an organ in the upper part of their skulls that inflates to hold the water they use in their attacks. This organ is extremely sensitive to vibrations in the air and is used as a pseudo ear.

```statblock
creature: "Quai Dau To"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
