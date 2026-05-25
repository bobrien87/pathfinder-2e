---
type: creature
group: ["Aberration", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Soulrider (Monitor)"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Aberration"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +4, Stealth +4"
abilityMods: ["+0", "+3", "+2", "-3", "+2", "-1"]
abilities_top:
  - name: "Planar Adaptation (Monitor)"
    desc: "A spawning soulrider has traits appropriate to the planar energy it's absorbed: celestial and holy, fiend and unholy, or monitor."
  - name: "Soul Attach"
    desc: "When a soulrider succeeds at a sucker Strike against a target with a soul capable of facing judgment, its sucker attaches it to that soul. While attached, both the soulrider and the host creature are [[Off Guard]], and the soulrider moves with its host until the soulrider dies or the host pulls it loose (`act escape dc=15`). If the host dies while the soulrider is attached, the soulrider disappears immediately to follow the soul leaving the body. A creature returned to life before reaching its final destination generally returns with any attached soulrider."
armorclass:
  - name: AC
    desc: "14; **Fort** +5, **Ref** +8, **Will** +2"
health:
  - name: HP
    desc: "8; **Weaknesses** spirit 1"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sucker +6 (`pf2:1`) (finesse, magical, reach 0 ft.), **Damage**  plus [[Soul Attach]]"
  - name: "Melee strike"
    desc: "Tail +6 (`pf2:1`) (agile, finesse, reach 0 ft., sanctified), **Damage** 1d4 bludgeoning plus 1 spirit"
spellcasting: []
abilities_bot:
  - name: "Monitor Escape"
    desc: "`pf2:2` The soulrider's form blurs as it exploits loopholes in the multiverse. It teleports to an empty space within 60 feet."
  - name: "Propulsive Launch"
    desc: "`pf2:2` The soulrider Leaps up to 40 feet, then makes a sucker Strike. If it's in the air and not attached to a creature after the Strike, it falls."
  - name: "Tail Thrash"
    desc: "`pf2:2` **Requirements** The soulrider is attached to a creature's soul <br>  <br> **Effect** The soulrider makes a tail Strike against the creature whose soul it's attached to, then one against another creature adjacent to the original target. These Strikes count towards the soulrider's multiple attack penalty, but it doesn't increase until after the second attack."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Although soulriders can grow quite large, most of them are narrow creatures only a few feet long. Even once they've attached to a soul and passed between planes, they must complete their adaptation to the new environment before beginning their growth.

These smallest soulriders might be found anywhere in the mortal Universe with a portal to the Outer Sphere or a history of summoning magic. Large batches of spawn in the wilderness are often culled by natural predators, but individual spawn can survive for years and travel many miles as they search for a host.

Resembling a lamprey or hagfish with a long whiplike tail, a soulrider uses its harmless sucker to hitch rides on a creature's soul. This seemingly simple connection transcends the physical, attaching directly to the host's soul and even riding along with the soul to its final destination. Once there, a soulrider leaves its host to absorb the surrounding planar energies, adapting to the new environment and growing large enough to produce spawn. However, it can only do so in the mortal Universe, so it must find a portal or other way to return. With this cycle, they've spread to every plane in the Outer Sphere, as well as many mortal worlds.

Although increasingly widespread, soulriders only appeared a little over a century ago. Thought to be a fleshwarper's attempt to cheat Pharasma's judgment by attaching several innocent souls to their own, soulriders' numbers have grown explosively since then.

Soulriders require little more than air to survive, but they're instinctually aware of their need for a mortal soul. Although their suckers are harmless, soulriders who feel threatened or become impatient will finish off their hosts or nearby threats with their tail.

```statblock
creature: "Soulrider (Monitor)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
