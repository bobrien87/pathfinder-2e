---
type: creature
group: ["Aberration", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Spawning Soulrider (Celestial)"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Aberration"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Stealth +6"
abilityMods: ["+1", "+3", "+4", "-2", "+3", "-1"]
abilities_top:
  - name: "Planar Adaptation (Celestial)"
    desc: "A spawning soulrider has traits appropriate to the planar energy it's absorbed: celestial and holy, fiend and unholy, or monitor."
  - name: "Swim the Dead Roads"
    desc: "In a process that takes 1 week, a spawning soulrider can travel through channels in the multiverse only it can sense, moving from the Outer Sphere plane whose energy it has absorbed to the Dead Roads that connect the Boneyard to the mortal Universe. From there, it travels to a random place in the Universe that can support life."
  - name: "Soul Attach"
    desc: "When a soulrider succeeds at a sucker Strike against a target with a soul capable of facing judgment, its sucker attaches it to that soul. While attached, both the soulrider and the host creature are [[Off Guard]], and the soulrider moves with its host until the soulrider dies or the host pulls it loose (`act escape dc=16`). If the host dies while the soulrider is attached, the soulrider disappears immediately to follow the soul leaving the body. A creature returned to life before reaching its final destination generally returns with any attached soulrider."
armorclass:
  - name: AC
    desc: "15; **Fort** +10, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "20; **Weaknesses** spirit 2"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sucker +8 (`pf2:1`) (finesse, magical), **Damage**  plus [[Soul Attach]]"
  - name: "Melee strike"
    desc: "Tail +8 (`pf2:1`) (agile, finesse, sanctified), **Damage** 1d4+1 bludgeoning plus 1 spirit"
spellcasting: []
abilities_bot:
  - name: "Celestial Flare"
    desc: "`pf2:2` Each enemy within 30 feet of the soulrider takes 2d6 spirit damage (DC 17 [[Will]] save). Creatures that fail the save are [[Blinded]] for 1 round. The spawning soulrider can't use Celestial Flare again for 1 minute."
  - name: "Grind Soul"
    desc: "`pf2:1` **Requirements** The spawning soulrider is attached to a creature's soul <br>  <br> **Effect** The soulrider grinds the creature's soul with its jagged inner mouth, dealing 2d8 spirit damage (DC 16 [[Will]] save). On a critical failure, the creature also takes 1d4 persistent,spirit damage. Regardless of the result, the spawning soulrider is no longer attached to the creature."
  - name: "Propulsive Launch"
    desc: "`pf2:2` The soulrider Leaps up to 40 feet, then makes a sucker Strike. If it's in the air and not attached to a creature after the Strike, it falls."
  - name: "Tail Thrash"
    desc: "`pf2:2` **Requirements** The soulrider is attached to a creature's soul <br>  <br> **Effect** The soulrider makes a tail Strike against the creature whose soul it's attached to, then one against another creature adjacent to the original target. These Strikes count towards the soulrider's multiple attack penalty, but it doesn't increase until after the second attack."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

When soulriders absorb sufficient planar energy, they become gravid with countless tiny eggs. Such soulriders instinctively return to the Universe via the Dead Roads to lay their spawn, although the exact metaphysical process has yet to be fully understood. Fiends and others keen to enter the mortal world have begun capturing and studying spawning soulriders, though such experiments carry their own risks, for soulriders prevented from returning to the Universe will continue to grow larger as they absorb more energy.

Once back in the Universe, spawning soulriders become fiercely protective of their near-translucent eggs and tiny spawn, using their remora-like maws to fend off potential threats. Anyone disturbing a soulrider in the process of spawning might find out what it feels like to have pieces of their soul torn away.

Resembling a lamprey or hagfish with a long whiplike tail, a soulrider uses its harmless sucker to hitch rides on a creature's soul. This seemingly simple connection transcends the physical, attaching directly to the host's soul and even riding along with the soul to its final destination. Once there, a soulrider leaves its host to absorb the surrounding planar energies, adapting to the new environment and growing large enough to produce spawn. However, it can only do so in the mortal Universe, so it must find a portal or other way to return. With this cycle, they've spread to every plane in the Outer Sphere, as well as many mortal worlds.

Although increasingly widespread, soulriders only appeared a little over a century ago. Thought to be a fleshwarper's attempt to cheat Pharasma's judgment by attaching several innocent souls to their own, soulriders' numbers have grown explosively since then.

Soulriders require little more than air to survive, but they're instinctually aware of their need for a mortal soul. Although their suckers are harmless, soulriders who feel threatened or become impatient will finish off their hosts or nearby threats with their tail.

```statblock
creature: "Spawning Soulrider (Celestial)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
