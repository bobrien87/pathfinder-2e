---
type: creature
group: ["Devil", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ort"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Devil"
trait_02: "Fiend"
trait_03: "Mindless"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+0; [[Greater Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +6"
abilityMods: ["+2", "+0", "+3", "-5", "+0", "-3"]
abilities_top:
  - name: "Subservience"
    desc: "Orts have little drive of their own, but other devils can take command of them. A non-ort devil can issue a command to all orts within 60 feet of it with a single action, which has the auditory and concentrate traits. The devil picks one of the following orders orts can understand, and the orts follow that order. The command and its effects end once the commander is out of the ort's sight, when a new command is issued by the same or another devil, or when the ort dies. <br>  <br> - **Kill** The ort attacks one target the commander singles out and gains a +1 circumstance bonus to attack rolls against the target. <br>  <br> - **Defend** The ort circles the commander and attacks any creature that comes near. It gains a +1 circumstance bonus to AC and saves. <br>  <br> - **Fetch** The ort gains a +10–foot circumstance bonus to its Speed and attempts to get an object or person the commander singles out. It attacks anyone and anything that gets in the way. <br>  <br> - **Work** The ort performs drudge work dictated by the commander."
armorclass:
  - name: AC
    desc: "13; **Fort** +9, **Ref** +6, **Will** +2"
health:
  - name: HP
    desc: "20; **Immunities** fire; **Weaknesses** holy 3; **Resistances** physical 3 except silver, poison 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +8 (`pf2:1`) (agile, magical, unarmed, unholy), **Damage** 1d4+2 slashing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These shapeless masses of quivering flesh are the least of devilkind. Pathetic creatures from Hell's first layer, orts roam alongside damned and suffering souls. Nessaris can combine the essence of a mob of orts to concentrate their collective wickedness within a single form, granting it an infernal sentience and transforming it into a more powerful devil (see the nessari's Shape Devils ability).

Masters of corruption and architects of conquest, devils seek both to tempt mortal life to join in their pursuit of all things profane and to spread tyranny throughout all worlds. The temptations they offer mortals range from great powers granted by the signing of an infernal contract to twisted favors following a whispered pledge to a diabolic patron, or any number of even subtler exchanges. Those who succumb to these temptations find themselves consigned to an afterlife of endless torment in the pits of Hell, wherein the only hope of escape lies in the chance of being promoted to become a devil in the infernal ranks.

Every devil has a specific role to play in the upkeep of the remorseless bureaucratic machine that is Hell, from soldiers and scholars to inquisitors, lawyers, judges, and executioners. Lowly orts perform subservient labor to more powerful and specialized devils, such as infantry and contract devils, while the greatest nessaris command entire infernal armies.

Asmodeus stands at the apex of the structure he created, but the layers below him are marked by a constant jockeying for position. Most diabolic plans ultimately serve to improve the schemer's place in the hierarchy.

```statblock
creature: "Ort"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
