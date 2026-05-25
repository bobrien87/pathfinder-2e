---
type: creature
group: ["Amphibious", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Athamaru Hunter"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Locathah"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]]"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +11, Diplomacy +5, Nature +7, Stealth +8, Survival +7"
abilityMods: ["+4", "+3", "+0", "+1", "+2", "+0"]
abilities_top:
  - name: "Cooperative Hunting"
    desc: "After the hunter attempts a Strike at a Large or larger target (regardless of success or failure), the next Strike one of the hunter's allies makes against the same target gains a +2 circumstance bonus to the attack roll."
  - name: "Fan Bolt"
    desc: "The hunter prepares their hooked crossbow bolts with carefully woven seaweed. <br>  <br> On a successful crossbow Strike, the bolt embeds and the seaweed fan deploys. The target takes a –10-foot status penalty to its swim Speed. A creature can Interact to attempt a DC 18 [[Athletics]] check, removing the bolt on a success. <br>  <br> > [!danger] Effect: Fan Bolt"
  - name: "Pack Attack"
    desc: "The hunter's Strikes deal an additional 1d8 damage to creatures within reach of at least two of the hunter's allies."
  - name: "Smooth Swimmer"
    desc: "The athamaru hunter ignores difficult terrain caused by aquatic terrain features."
armorclass:
  - name: AC
    desc: "20; **Fort** +7, **Ref** +10, **Will** +9"
health:
  - name: HP
    desc: "38"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +11 (`pf2:1`) (reach 10 ft.), **Damage** 1d8+4 piercing"
  - name: "Ranged strike"
    desc: "Crossbow +10 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8 piercing plus [[Fan Bolt]]"
spellcasting: []
abilities_bot:
  - name: "Hunt Prey"
    desc: "`pf2:1` The athamaru hunter designates a single creature they can see and hear, or one they're Tracking, as their prey. The hunter gains a +2 circumstance bonus to Perception checks to [[Seek]] the prey and to Survival checks to [[Track]] the prey. <br>  <br> The first time the athamaru hits their designated prey in a round, they deal an additional 1d8 precision damage. These effects last until the hunter uses Hunt Prey again."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Deep in the sea, schools of athamarus—piscine humanoids armed with spears and specialized crossbows—stalk sharks, sea serpents, and giant squid from the backs of their giant moray eel mounts. The first hunters to strike are armed with barbed harpoons that deploy large fans of seaweed, slowing and exhausting their prey. A daring few athamarus use the embedded harpoon as a handle to ride prey for a short time. Once the creature is tired, remaining hunters finish it with longspears. Athamarus developed this hunting tradition to forge skilled warriors and deter potential attackers, partially in response to centuries of oppression and mistreatment from other aquatic cultures.

Athamarus rarely hunt land-dwellers, instead offering to trade their services as guides in exchange for metal and ceramic items they can't build underwater—and for tubers, which they consider earthy delicacies. They render aid to damaged sailing ships and rescue shipwrecked sailors, providing food and guidance.

Athamaru communities—usually villages of 200 individuals or fewer—are matriarchal. The ruler of a given community is also the primary egg-layer, providing each generation with powerful familial bonds. The communities are tight-knit and loyal. Matriarchs are advised and assisted by primal spellcasters and healers.

```statblock
creature: "Athamaru Hunter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
