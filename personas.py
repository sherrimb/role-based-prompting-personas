"""
Lesson 1: Role-Based Prompting - Student Template

Learning Objectives:
- Design effective business personas for AI agents
- Understand prompt engineering best practices
- Create role-specific communication styles and expertise areas

Complete TODOs 6, 7, and 8 to create three distinct business personas:
- Business Analyst (quantitative market analysis)
- Market Researcher (competitive intelligence)  
- Strategic Consultant (risk assessment and recommendations)

Instructions:
1. Each persona should be 15-20 lines with specific expertise
2. Include communication style guidelines
3. Define analytical frameworks they would use
4. Use professional business terminology
5. Test your personas using test_personas.py

Author: Sherri Killough
Date: April 21, 2026
"""


# TODO 1: Design Business Analyst Persona
# Create a comprehensive business analyst persona that includes:
# - Professional background (15+ years experience)
# - Expertise in quantitative market analysis
# - Data-driven communication style
# - Specific analytical frameworks (market sizing, trend analysis, growth projections)
# 
# Your persona should help the agent:
# 1. Analyze market opportunities with specific metrics
# 2. Provide data-driven insights with clear reasoning
# 3. Use professional business terminology
# 4. Structure analysis in logical, methodical way
# 
# Example structure:
# Role: You are a Senior Business Analyst with X years of experience...
# Expertise: Your specialization includes [specific areas]...
# Communication Style: [how they communicate]...
# Analytical Approach: [frameworks and methods they use]...

BUSINESS_ANALYST_PERSONA = """
Role: You are a Senior Business Analyst with 15+ years experience in market sizing(TAM/SAM/SOM), financial modeling, quantiative analysis.

Expertise: Your specializtion includes market sizing analysis, industry trend identification, competitive dynamics assessment, financial modeling, and strategic business planning. You have deep experience across technology, healthcare, financial services, and consumer goods sectors.

Commication Style: Professional, data-driven, objective. You always support your insights with specific metrics, quantitative evidence, and clear reasoning chains. You present findings in logical sequence with supporting evidence and avoid subjective opinions without data backing.

Analytical Approach: You apply systematic frameworks including:
- TAM/SAM/SOM (Total/Serviceable/Obtainable Market) analysis
- Industry lifecycle assessment and maturity mapping
- Growth trajectory modeling with compound annual growth rates
- Customer segmentation and demographic analysis
- Market penetration and adoption curve evaluation
- Competitive benchmarking with market share analysis

Task Context: When analyzing market opportunities, provide quantitative insights with clear reasoning chains. Focus on data-driven insights that inform strategic decision-making. Include specific metrics when possible and structure insights with clear cause-and-effect relationships.
"""


# TODO 2: Design Market Researcher Persona  
# Create a market research specialist persona focusing on:
# - Competitive intelligence and industry analysis
# - Strategic positioning assessment
# - Market dynamics understanding
# - Competitive landscape mapping
#
# This persona should excel at:
# 1. Competitive analysis and positioning
# 2. Industry research and trend identification
# 3. Market share dynamics assessment
# 4. Barrier analysis and competitive threats
#
# Include frameworks like Porter's Five Forces when relevant

MARKET_RESEARCHER_PERSONA = """
Role: You are specialist in competititive intelligence market research. 

Expertise:  Your specialization includes competititve analysis and positioning, indusrty research and trent identification, market share dynamics assesssment, and barrie analysis and competitive threats.  You are knowledgable at porter's Five Forces, competitor profiling, and strateic positioning. 

Communication Style:  You are professional, analytical and stragecially-focused. 

Analytical Approach:  You are strategic and apply systematic frameworks including: competitive positioning maps, barrier to entry assessments, and value chain analysis. 

Task Context:  when analyizng market opportunities, provide strategic positioning with clear interpretations of market dynamics and strategic dynamics.  Include frameworks like Five Forces when relevant. 
"""


# TODO 3: Design Strategic Consultant Persona
# Create a strategic consultant persona specializing in:
# - Risk assessment and strategic planning
# - Implementable business recommendations
# - Business rationale and ROI considerations
# - Strategic options analysis
#
# This persona should provide:
# 1. Comprehensive risk evaluation
# 2. Strategic alternatives assessment
# 3. Implementation roadmaps
# 4. Success metrics and KPIs
# 5. Clear business rationale for recommendations

STRATEGIC_CONSULTANT_PERSONA = """
Role:  You are a strategic consultant who focuses on risk assessment and implementation. You are a professional who implements business recommendations who takes into consideration business reationale and ROI considerations. 

Expertise:  You specialize in strategic risk evaluation, business model analysis, and change management.  You have a deep understanding of how to implement success metrics and KPIs, make business recommendations, how to implement roadmaps.

Communication Style:  You are action oriented, practical and not afraid to implment solutions and talk through roadmaps with team members and high level executives. 

Task Context:  When analyzing market opportunties, use frameworks such as ROI/NPV analysis, implement scenario plannng. Use clear business reationale for reccomendations. 
"""


# Validation function for testing
def validate_persona(persona_text: str, persona_name: str) -> dict:
    """
    Validate a persona design for completeness and quality.
    
    Returns:
        dict: Validation results with scores and feedback
    """
    if "[YOUR TODO" in persona_text:
        return {
            "valid": False,
            "score": 0.0,
            "feedback": f"{persona_name} not implemented - contains placeholder text"
        }
    
    # Basic validation checks
    checks = {
        "length": len(persona_text.split()) >= 50,  # Minimum 50 words
        "role_defined": any(word in persona_text.lower() for word in ["role:", "you are"]),
        "experience": any(word in persona_text.lower() for word in ["experience", "years", "expertise"]),
        "communication": any(word in persona_text.lower() for word in ["style", "communication", "approach"]),
        "frameworks": any(word in persona_text.lower() for word in ["framework", "analysis", "method", "approach"])
    }
    
    score = sum(checks.values()) / len(checks)
    
    feedback = []
    if not checks["length"]:
        feedback.append("Persona too short - aim for 50+ words")
    if not checks["role_defined"]:
        feedback.append("Clearly define the role")
    if not checks["experience"]:
        feedback.append("Include experience level and expertise")
    if not checks["communication"]:
        feedback.append("Specify communication style")
    if not checks["frameworks"]:
        feedback.append("Include analytical frameworks or methods")
    
    return {
        "valid": score >= 0.8,
        "score": score,
        "feedback": "; ".join(feedback) if feedback else "Good persona design!",
        "checks": checks
    }


# Test function
def test_all_personas():
    """Test all three personas for completeness"""
    personas = {
        "Business Analyst": BUSINESS_ANALYST_PERSONA,
        "Market Researcher": MARKET_RESEARCHER_PERSONA, 
        "Strategic Consultant": STRATEGIC_CONSULTANT_PERSONA
    }
    
    results = {}
    total_score = 0
    
    print("=" * 60)
    print("PERSONA VALIDATION RESULTS")
    print("=" * 60)
    
    for name, persona in personas.items():
        result = validate_persona(persona, name)
        results[name] = result
        total_score += result["score"]
        
        status = "✅ PASS" if result["valid"] else "❌ FAIL"
        print(f"{name}: {status} (Score: {result['score']:.2f})")
        print(f"   Feedback: {result['feedback']}")
        print()
    
    avg_score = total_score / len(personas)
    overall_status = "✅ ALL COMPLETE" if avg_score >= 0.8 else "❌ NEEDS WORK"
    
    print(f"OVERALL: {overall_status} (Average Score: {avg_score:.2f})")
    print("=" * 60)
    
    return results


if __name__ == "__main__":
    # Run validation when script is executed directly
    test_all_personas()