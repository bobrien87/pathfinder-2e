---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zecui"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +15, Crafting +12, Medicine +14, Stealth +17"
abilityMods: ["+3", "+5", "+2", "+0", "+2", "+0"]
abilities_top:
  - name: "Spit Mucus"
    desc: "A creature hit by the zecui's spit attack is [[Immobilized]] by the larva-infested mucus and stuck to the nearest surface until it Escapes. While that creature is immobilized, it is exposed to zecui larvae at the end of each of its turns."
  - name: "Zecui Larvae"
    desc: "**Saving Throw** DC 25 [[Fortitude]] save <br>  <br> **Stage 1** visible lumps as the larvae move but no ill effect (1 day) <br>  <br> **Stage 2** [[Drained]] 1 (1 day) <br>  <br> **Stage 3** [[Drained]] 2 (1 day) <br>  <br> **Stage 4** [[Drained]] 3 and controlled by the zecui larva (1 day) <br>  <br> **Stage 5** the creature dies and the adult zecui can emerge from the corpse as an Interact action"
armorclass:
  - name: AC
    desc: "23; **Fort** +14, **Ref** +17, **Will** +12"
health:
  - name: HP
    desc: "110"
abilities_mid:
  - name: "Preserve Prey"
    desc: "`pf2:r` **Trigger** A living creature within 30 feet is reduced to 0 Hit Points <br>  <br> **Effect** The zecui channels corrupt vitality into the triggering creature, which still goes [[Unconscious]] but does not gain the dying condition. While that creature is unconscious, the residual energy attempts to counteract any vitality spell healing that creature with a +15 counteract modifier."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +17 (`pf2:1`) (agile, finesse, versatile s), **Damage** 2d6+7 piercing"
  - name: "Melee strike"
    desc: "Mandibles +15 (`pf2:1`), **Damage** 2d8+7 piercing"
  - name: "Melee strike"
    desc: "Claws +17 (`pf2:1`) (agile, finesse), **Damage** 2d4+7 slashing plus [[Grab]]"
  - name: "Ranged strike"
    desc: "Spit +17 (`pf2:1`), **Damage**  plus [[Spit Mucus]]"
spellcasting: []
abilities_bot:
  - name: "Dual Stab"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Effect** The zecui makes two shortsword Strikes against an [[Immobilized]] or [[Off Guard]] target. These strikes count towards the zecui's multiple attack penalty, but it doesn't increase until after the second attack."
  - name: "Harden Chitin"
    desc: "`pf2:1` The zecui fuses much of their chitin into a black metallic shell. They gain resistance 5 to all damage (except mental and spirit) until they next take a move action."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These chitinous entities can only grow to adulthood within a host creature, usually a humanoid or larger animal. When such hosts are particularly plentiful, zecuis can multiply at a horrifying rate, sealing hosts in subterranean chambers until their larvae grow to adulthood. However, during lean times, zecui adults will sate their hunger by eating those hosts along with any unlucky larvae gestating within, unable to be infested by their own young.

Between periods of wakefulness, zecuis hibernate for decades in burrows or buried within the soil. Sometimes an unincubated larva will be buried this way, waiting for a living host to come in contact with it. Once a zecui larva has gestated long enough to take control of its host, it may seek out larger and more powerful entities to devour the host, transferring themselves to a more plentiful source of food.

```statblock
creature: "Zecui"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
