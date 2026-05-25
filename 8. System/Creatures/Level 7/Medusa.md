---
type: creature
group: ["Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Medusa"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +16, Diplomacy +14, Stealth +16"
abilityMods: ["+2", "+5", "+4", "+2", "+1", "+2"]
abilities_top:
  - name: "Serpent Venom"
    desc: "**Saving Throw** DC 25 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d6 poison damage and [[Enfeebled]] 2 (1 round)"
armorclass:
  - name: AC
    desc: "25 all-around vision; **Fort** +15, **Ref** +16, **Will** +14"
health:
  - name: HP
    desc: "105"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Biting Snakes"
    desc: "`pf2:r` **Trigger** A creature ends its turn adjacent to the medusa. <br>  <br> **Effect** The medusa makes a snake fangs Strike against the creature."
  - name: "Petrifying Gaze"
    desc: "30 feet. <br>  <br> When a creature ends its turn in the aura, it must attempt a DC 25 [[Fortitude]] save. If the creature fails, it becomes [[Slowed]] 1 for 1 minute. <br>  <br> The medusa can deactivate or activate this aura by using a single action, which has the concentrate trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +18 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+8 piercing plus [[Serpent Venom]]"
  - name: "Melee strike"
    desc: "Snake Fangs +16 (`pf2:1`) (agile, finesse), **Damage** 1d4+8 piercing plus [[Serpent Venom]]"
  - name: "Ranged strike"
    desc: "Composite Shortbow +19 (`pf2:1`) (deadly d10, magical, propulsive, reload 0, range 60 ft.), **Damage** 1d6+7 piercing plus [[Serpent Venom]]"
spellcasting: []
abilities_bot:
  - name: "Focus Gaze"
    desc: "`pf2:1` The medusa fixes their glare at a creature they can see within 30 feet. The target must immediately attempt a DC 25 [[Fortitude]] save against the medusa's petrifying gaze. <br>  <br> If the creature was already [[Slowed]] by petrifying gaze before attempting its save, a failed save causes it to be [[Petrified]] permanently. After attempting its save, the creature is then temporarily immune until the start of the medusa's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Monstrous humanoids that resemble humans with snakes instead of hair, medusas are best known for their petrifying gazes that—if lingered upon—can permanently transform mortals to stone. Medusas are shrewd and manipulative adversaries who collect and covet secrets, and who use threats and guile to exploit the fears of weaker creatures. A medusa may seek out powerful magic items, use divining magic to discover secret knowledge and unlock forbidden power, or infiltrate a society to beguile influential politicians. Their ability to worm their way into powerful organizations makes them natural leaders of criminal outfits and thieves' guilds, and their interest in magical phenomena leads some to pursue careers as oracles who offer to help adventurers find what they seek—for a price. Of course, if wit and deception prove insufficient, a medusa can always simply turn rivals into ornate stone decorations with little more than a glare. Many medusas build elaborate lairs to call home, often decorated with the statues of their foes turned into macabre trophies on prominent display.

Exceptionally agile and surprisingly hardy, a medusa rarely backs down from a conflict, even when cornered. Many adventurers who thought themselves readied to resist the effects of a medusa's gaze have nevertheless fallen to a medusa, as these creatures are also often deadly archers able to riddle their foes with venom-coated arrows from a distance. Still, a medusa may barter for their life if no alternatives remain, and the secrets carried by these powerful villains often make it more than worth sparing their lives.

```statblock
creature: "Medusa"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
