---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Katpaskir"
level: "18"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+31; [[Darkvision]], [[See Invisibility]]"
languages: "Aklo, Chthonian, Common, Draconic, Empyrean (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +31, Arcana +35, Deception +31, Occultism +33, Religion +32, Stealth +31, Thievery +31"
abilityMods: ["+6", "+5", "+9", "+7", "+6", "+5"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "41; **Fort** +35, **Ref** +29, **Will** +30"
health:
  - name: HP
    desc: "415; **Immunities** poison; **Weaknesses** cold iron 15, holy 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Breach Planar Wards"
    desc: "`pf2:0` **Trigger** An effect attempts to prevent the katpaskir from using a teleportation effect or from casting [[Summon Fiend]] <br>  <br> **Effect** The katpaskir attempts to counteract the triggering effect (counteract modifier of +29). The katpaskir automatically fails against an artifact's effect."
  - name: "Distortion Field"
    desc: "30 feet. Reality bends and warps on the level of all senses without displacing the katpaskir's actual location. Creatures of the katpaskir's choice who start their turn in the aura must succeed at a DC 37 [[Will]] save or treat the area as greater difficult terrain and uneven ground (DC 20). A creature who succeeds still treats the area as difficult terrain. For such creatures, the distance through the aura is doubled for determining range penalty."
  - name: "Mirrored Summons"
    desc: "`pf2:r` **Trigger** A creature within 30 feet that the katpaskir is aware of casts [[Summon Celestial]] or otherwise summons a holy creature <br>  <br> **Effect** The katpaskir casts summon fiend, regaining the daily ability to do so if needed. This effect is automatically sustained as long as the triggering summoning is sustained, for up to 1 minute."
  - name: "Warp Sense"
    desc: "The katpaskir senses changes in the planar fabric within 1 mile, including any teleportation effect, sensing the direction and distance to the disturbance. If it senses such a disturbance within 500 feet, the katpaskir can cast [[Scouting Eye]] to observe the area without needing line of sight to the location."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +34 (`pf2:1`) (magical, unarmed, unholy), **Damage** 3d12+14 slashing plus 1d6 spirit"
  - name: "Melee strike"
    desc: "Talon +34 (`pf2:1`) (agile, magical, unarmed, unholy), **Damage** 3d8+14 slashing plus 1d6 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 40, attack +32<br>**7th** [[Interplanar Teleport]]<br>**6th** [[Disintegrate]], [[Teleport]]<br>**5th** [[Banishment]], [[Scouting Eye]] (At Will), [[Summon Fiend (Demons only)]]<br>**4th** [[Flicker]], [[Planar Tether]] (At Will), [[Translocate]] (At Will), [[Unfettered Movement]] (Constant)<br>**2nd** [[See the Unseen]] (Constant)"
abilities_bot:
  - name: "Dimensional Ambush"
    desc: "`pf2:2` The katpaskir casts [[Translocate]], then makes a melee Strike that deals three extra dice of damage. This Strike counts as two attacks when calculating the katpaskir's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Born of the souls of doomsayers and cult leaders who sought to undermine and unravel reality, katpaskirs are demons of nihilism and unmaking. They pry into the edges of reality, placing themselves into the cracks between realms and scratching away at the composure of existence itself. Katpaskirs have an uncanny sense for locating portals and other planar convergences. They seek to corrupt and expand these gateways, setting them loose to expand on their own or drift across the multiverse. As they do, they slowly contribute to the ultimate unraveling of reality. Katpaskirs often appear as insectile humanoids with multiple arms or legs, each capable of scratching and clawing away at the seams of existence.

```statblock
creature: "Katpaskir"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
